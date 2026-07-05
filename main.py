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
    )

    feeding = Task(
        name="Breakfast feeding",
        category="Feeding",
        duration_minutes=10,
        priority=5,
        time="09:00",
    )

    grooming = Task(
        name="Brush fur",
        category="Grooming",
        duration_minutes=20,
        priority=3,
        time="11:00",
    )

    medication = Task(
        name="Give medication",
        category="Medication",
        duration_minutes=5,
        priority=4,
        time="09:00",
    )

    dog.add_task(walk)
    dog.add_task(feeding)
    cat.add_task(grooming)
    cat.add_task(medication)

    scheduler = Scheduler(available_minutes=45)

    for task in owner.get_all_tasks():
        scheduler.add_task(task)

    daily_plan = scheduler.generate_daily_plan()
    conflicts = scheduler.detect_conflicts()

    print(f"Today's Schedule for {owner.name}")
    print("-" * 35)

    for task in daily_plan:
        print(
            f"{task.time} — {task.name} "
            f"({task.duration_minutes} min) "
            f"[priority: {task.priority}]"
        )

    print("\nConflicts:")
    if conflicts:
        for conflict in conflicts:
            print(conflict)
    else:
        print("No conflicts found.")


if __name__ == "__main__":
    main()