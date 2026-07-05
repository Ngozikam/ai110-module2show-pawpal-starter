from pawpal_system import Pet, Task


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