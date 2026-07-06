from dataclasses import dataclass, field
from datetime import date, timedelta
from typing import List


@dataclass
class Task:
    """Represents one pet care activity."""

    name: str
    category: str
    duration_minutes: int
    priority: int
    time: str = "Anytime"
    frequency: str = "daily"
    completed: bool = False
    due_date: date = field(default_factory=date.today)
    pet_name: str = "Unknown"

    def mark_complete(self) -> None:
        """Mark the task as completed."""
        self.completed = True

    def is_high_priority(self) -> bool:
        """Return True if the task is high priority."""
        return self.priority >= 4

    def create_next_occurrence(self):
        """Create the next recurring task based on frequency."""
        if self.frequency == "daily":
            next_date = self.due_date + timedelta(days=1)
        elif self.frequency == "weekly":
            next_date = self.due_date + timedelta(weeks=1)
        else:
            return None

        return Task(
            name=self.name,
            category=self.category,
            duration_minutes=self.duration_minutes,
            priority=self.priority,
            time=self.time,
            frequency=self.frequency,
            due_date=next_date,
            pet_name=self.pet_name,
        )


@dataclass
class Pet:
    """Stores pet details and care tasks."""

    name: str
    species: str
    breed: str
    age: int
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a task to this pet."""
        self.tasks.append(task)

    def get_tasks(self) -> List[Task]:
        """Return all tasks assigned to this pet."""
        return self.tasks


@dataclass
class Owner:
    """Manages pet owner information and pets."""

    name: str
    preferences: str
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to this owner."""
        self.pets.append(pet)

    def get_pets(self) -> List[Pet]:
        """Return all pets owned by this owner."""
        return self.pets

    def get_all_tasks(self) -> List[Task]:
        """Return all tasks across all pets."""
        all_tasks = []
        for pet in self.pets:
            all_tasks.extend(pet.get_tasks())
        return all_tasks


@dataclass
class Scheduler:
    """Organizes pet care tasks into a daily plan."""

    available_minutes: int
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a task to the scheduler."""
        self.tasks.append(task)

    def sort_tasks_by_priority(self) -> List[Task]:
        """Sort tasks from highest to lowest priority."""
        return sorted(self.tasks, key=lambda task: task.priority, reverse=True)
    
    def sort_by_time(self) -> List[Task]:
        """Sort tasks by scheduled time."""
        return sorted(
            self.tasks,
            key=lambda task: task.time if task.time != "Anytime" else "99:99"
        )

    def filter_by_completion(self, completed: bool = False) -> List[Task]:
        """Filter tasks by completion status."""
        return [task for task in self.tasks if task.completed == completed]

    def filter_by_pet(self, pet_name: str) -> List[Task]:
        """Filter tasks by pet name."""
        return [
            task for task in self.tasks
            if task.pet_name.lower() == pet_name.lower()
        ]

    def complete_task_and_recur(self, task: Task) -> None:
        """Mark a task complete and add its next recurring occurrence."""
        task.mark_complete()
        next_task = task.create_next_occurrence()
        if next_task:
            self.add_task(next_task)

    def generate_daily_plan(self) -> List[Task]:
        """Generate a plan that fits within the available time."""
        plan = []
        used_minutes = 0

        for task in self.sort_tasks_by_priority():
            if used_minutes + task.duration_minutes <= self.available_minutes:
                plan.append(task)
                used_minutes += task.duration_minutes

        return plan

    def detect_conflicts(self) -> List[str]:
        """Detect tasks that share the same time."""
        seen_times = {}
        conflicts = []

        for task in self.tasks:
            if task.time in seen_times:
                conflicts.append(
                    f"Conflict: {task.name} and {seen_times[task.time]} are both scheduled at {task.time}."
                )
            else:
                seen_times[task.time] = task.name

        return conflicts