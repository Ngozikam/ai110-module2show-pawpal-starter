from datetime import date, timedelta

from pawpal_system import Pet, Scheduler, Task


def test_task_completion_changes_status():
    task = Task(
        name="Morning walk",
        category="Exercise",
        duration_minutes=30,
        priority=5,
    )

    task.mark_complete()

    assert task.completed is True


def test_adding_task_to_pet_increases_task_count():
    pet = Pet(name="Biscuit", species="Dog", breed="Golden Retriever", age=3)

    task = Task(
        name="Breakfast feeding",
        category="Feeding",
        duration_minutes=10,
        priority=5,
    )

    pet.add_task(task)

    assert len(pet.tasks) == 1


def test_sort_by_time_returns_tasks_in_chronological_order():
    scheduler = Scheduler(available_minutes=60)

    task_late = Task(
        name="Evening walk",
        category="Exercise",
        duration_minutes=20,
        priority=3,
        time="18:00",
    )

    task_early = Task(
        name="Breakfast feeding",
        category="Feeding",
        duration_minutes=10,
        priority=5,
        time="08:00",
    )

    scheduler.add_task(task_late)
    scheduler.add_task(task_early)

    sorted_tasks = scheduler.sort_by_time()

    assert sorted_tasks[0].name == "Breakfast feeding"
    assert sorted_tasks[1].name == "Evening walk"


def test_daily_recurring_task_creates_next_day_task():
    scheduler = Scheduler(available_minutes=60)

    task = Task(
        name="Morning walk",
        category="Exercise",
        duration_minutes=30,
        priority=5,
        time="08:00",
        frequency="daily",
        due_date=date.today(),
    )

    scheduler.add_task(task)
    scheduler.complete_task_and_recur(task)

    assert task.completed is True
    assert len(scheduler.tasks) == 2
    assert scheduler.tasks[1].due_date == date.today() + timedelta(days=1)


def test_conflict_detection_flags_duplicate_times():
    scheduler = Scheduler(available_minutes=60)

    task_one = Task(
        name="Breakfast feeding",
        category="Feeding",
        duration_minutes=10,
        priority=5,
        time="09:00",
    )

    task_two = Task(
        name="Give medication",
        category="Medication",
        duration_minutes=5,
        priority=4,
        time="09:00",
    )

    scheduler.add_task(task_one)
    scheduler.add_task(task_two)

    conflicts = scheduler.detect_conflicts()

    assert len(conflicts) == 1
    assert "09:00" in conflicts[0]


def test_filter_by_pet_returns_only_matching_pet_tasks():
    scheduler = Scheduler(available_minutes=60)

    dog_task = Task(
        name="Morning walk",
        category="Exercise",
        duration_minutes=30,
        priority=5,
        pet_name="Biscuit",
    )

    cat_task = Task(
        name="Brush fur",
        category="Grooming",
        duration_minutes=20,
        priority=3,
        pet_name="Luna",
    )

    scheduler.add_task(dog_task)
    scheduler.add_task(cat_task)

    filtered_tasks = scheduler.filter_by_pet("Biscuit")

    assert len(filtered_tasks) == 1
    assert filtered_tasks[0].pet_name == "Biscuit"


def test_daily_plan_respects_available_minutes():
    scheduler = Scheduler(available_minutes=40)

    high_priority_task = Task(
        name="Morning walk",
        category="Exercise",
        duration_minutes=30,
        priority=5,
    )

    medium_priority_task = Task(
        name="Breakfast feeding",
        category="Feeding",
        duration_minutes=10,
        priority=3,
    )

    low_priority_task = Task(
        name="Brush fur",
        category="Grooming",
        duration_minutes=20,
        priority=1,
    )

    scheduler.add_task(high_priority_task)
    scheduler.add_task(medium_priority_task)
    scheduler.add_task(low_priority_task)

    plan = scheduler.generate_daily_plan()

    assert len(plan) == 2
    assert sum(task.duration_minutes for task in plan) <= 40
    assert high_priority_task in plan
    assert medium_priority_task in plan