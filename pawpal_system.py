from dataclasses import dataclass, field
from typing import List


@dataclass
class Task:
    name: str
    category: str
    duration_minutes: int
    priority: int
    completed: bool = False

    def mark_complete(self) -> None:
        pass

    def is_high_priority(self) -> bool:
        pass


@dataclass
class Pet:
    name: str
    species: str
    breed: str
    age: int
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        pass

    def get_tasks(self) -> List[Task]:
        pass


@dataclass
class Owner:
    name: str
    preferences: str
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        pass

    def get_pets(self) -> List[Pet]:
        pass


@dataclass
class Scheduler:
    available_minutes: int
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        pass

    def sort_tasks_by_priority(self) -> List[Task]:
        pass

    def generate_daily_plan(self) -> List[Task]:
        pass

    def detect_conflicts(self) -> List[Task]:
        pass