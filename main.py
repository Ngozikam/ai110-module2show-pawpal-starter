from pawpal_system import Owner, Pet, Task, Scheduler


def main():
    owner = Owner(name="Blessing", preferences="Prioritize health and morning care.")

    dog = Pet(name="Biscuit", species="Dog", breed="Golden Retriever", age=3)
    cat = Pet(name="Luna", species="Cat", breed="Tabby", age=2)

    owner.add_pet(dog)
    owner.add_pet(cat)

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

    dog.add_task(walk)
    dog.add_task(feeding)
    cat.add_task(grooming)
    cat.add_task(medication)

    scheduler = Scheduler(available_minutes=75)

    for task in owner.get_all_tasks():
        scheduler.add_task(task)

    print("Tasks Sorted by Time")
    print("-" * 35)
    for task in scheduler.sort_by_time():
        print(f"{task.time} — {task.name} ({task.pet_name})")

    print("\nIncomplete Tasks")
    print("-" * 35)
    for task in scheduler.filter_by_completion(completed=False):
        print(f"{task.name} [{task.completed}]")

    print("\nTasks for Biscuit")
    print("-" * 35)
    for task in scheduler.filter_by_pet("Biscuit"):
        print(task.name)

    print("\nToday's Schedule")
    print("-" * 35)
    for task in scheduler.generate_daily_plan():
        print(
            f"{task.time} — {task.name} "
            f"({task.duration_minutes} min) "
            f"[priority: {task.priority}]"
        )

    print("\nRecurring Task Demo")
    print("-" * 35)
    scheduler.complete_task_and_recur(walk)
    print(f"Completed: {walk.name} = {walk.completed}")
    print(f"Total tasks after recurrence: {len(scheduler.tasks)}")

    print("\nConflicts")
    print("-" * 35)
    conflicts = scheduler.detect_conflicts()
    if conflicts:
        for conflict in conflicts:
            print(conflict)
    else:
        print("No conflicts found.")


if __name__ == "__main__":
    main()