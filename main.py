from pawpal_system import Owner, Pet, Task, Scheduler
from tabulate import tabulate


def main():
    """Run the PawPal+ command-line demonstration."""

    # Create the owner
    owner = Owner(
        name="Blessing",
        preferences="Prioritize health and morning care."
    )

    # Create pets
    dog = Pet(
        name="Biscuit",
        species="Dog",
        breed="Golden Retriever",
        age=3
    )

    cat = Pet(
        name="Luna",
        species="Cat",
        breed="Tabby",
        age=2
    )

    owner.add_pet(dog)
    owner.add_pet(cat)

    # Create pet care tasks
    walk = Task(
        name="Morning walk",
        category="Exercise",
        duration_minutes=30,
        priority=5,
        time="08:00",
        frequency="daily",
        pet_name="Biscuit",
    )

    feeding = Task(
        name="Breakfast feeding",
        category="Feeding",
        duration_minutes=10,
        priority=5,
        time="09:00",
        frequency="daily",
        pet_name="Biscuit",
    )

    grooming = Task(
        name="Brush fur",
        category="Grooming",
        duration_minutes=20,
        priority=3,
        time="11:00",
        frequency="weekly",
        pet_name="Luna",
    )

    medication = Task(
        name="Give medication",
        category="Medication",
        duration_minutes=5,
        priority=4,
        time="09:00",
        frequency="daily",
        pet_name="Luna",
    )

    # Assign tasks to pets
    dog.add_task(walk)
    dog.add_task(feeding)
    cat.add_task(grooming)
    cat.add_task(medication)

    # Create the scheduler
    scheduler = Scheduler(available_minutes=75)

    # Add all owner tasks to the scheduler
    for task in owner.get_all_tasks():
        scheduler.add_task(task)

    # Demonstrate time-based sorting
    print("Tasks Sorted by Time")
    print("-" * 35)

    for task in scheduler.sort_by_time():
        print(f"{task.time} — {task.name} ({task.pet_name})")

    # Demonstrate advanced priority scheduling
    print("\n🐾 Priority-Based Schedule")
    print("-" * 35)

    priority_rows = []

    for task in scheduler.sort_by_priority_then_time():
        priority_rows.append(
            [
                task.time,
                task.name,
                task.pet_name,
                task.duration_minutes,
                task.priority_label(),
            ]
        )

    print(
        tabulate(
            priority_rows,
            headers=["Time", "Task", "Pet", "Duration", "Priority"],
            tablefmt="grid",
        )
    )

    # Demonstrate completion filtering
    print("\nIncomplete Tasks")
    print("-" * 35)

    for task in scheduler.filter_by_completion(completed=False):
        print(f"{task.name} [{task.completed}]")

    # Demonstrate filtering by pet
    print("\nTasks for Biscuit")
    print("-" * 35)

    for task in scheduler.filter_by_pet("Biscuit"):
        print(task.name)

    # Generate the daily schedule
    print("\nToday's Schedule")
    print("-" * 35)

    for task in scheduler.generate_daily_plan():
        print(
            f"{task.time} — {task.name} "
            f"({task.duration_minutes} min) "
            f"[priority: {task.priority}]"
        )

    # Demonstrate recurring task behavior
    print("\nRecurring Task Demo")
    print("-" * 35)

    scheduler.complete_task_and_recur(walk)

    print(f"Completed: {walk.name} = {walk.completed}")
    print(f"Total tasks after recurrence: {len(scheduler.tasks)}")

    # Demonstrate conflict detection
    print("\nConflicts")
    print("-" * 35)

    conflicts = scheduler.detect_conflicts()

    if conflicts:
        for conflict in conflicts:
            print(conflict)
    else:
        print("No conflicts found.")

    # Demonstrate next available slot
    print("\n⏰ Next Available Slot")
    print("-" * 35)

    next_slot = scheduler.find_next_available_slot()

    print(f"✅ Recommended next available time: {next_slot}")

    # Demonstrate data persistence
    print("\nData Persistence")
    print("-" * 35)

    owner.save_to_json("data.json")
    print("PawPal+ data saved to data.json.")

    loaded_owner = Owner.load_from_json("data.json")

    print(f"Loaded owner: {loaded_owner.name}")
    print(f"Loaded pets: {len(loaded_owner.pets)}")
    print(f"Loaded tasks: {len(loaded_owner.get_all_tasks())}")


if __name__ == "__main__":
    main()