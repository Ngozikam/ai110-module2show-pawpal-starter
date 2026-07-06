# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

```text
Today's Schedule for Blessing
-----------------------------------
08:00 — Morning walk (30 min) [priority: 5]
09:00 — Breakfast feeding (10 min) [priority: 5]
09:00 — Give medication (5 min) [priority: 4]

Conflicts:
Conflict: Give medication and Breakfast feeding are both scheduled at 09:00.
```

## 🧪 Testing PawPal+

Run the full test suite:

```bash
python -m pytest
```

Run with coverage:

```bash
pytest --cov
```

### What the tests verify

- Task completion updates the completion status.
- Adding a task increases the pet's task count.
- Tasks are sorted correctly by scheduled time.
- Daily recurring tasks automatically create a new task for the next day.
- Conflict detection identifies duplicate scheduled times.
- Filtering returns tasks for the selected pet only.
- Daily scheduling respects the owner's available time.

### Successful test run

```text
platform win32 -- Python 3.13.1, pytest-9.1.1, pluggy-1.6.0
rootdir: C:\Users\OWNER\Documents\GitHub\ai110-module2show-pawpal-starter
plugins: anyio-4.14.1
collected 7 items

tests\test_pawpal.py .......

==================== 7 passed in 0.17s ====================
```

**Confidence Level:** ⭐⭐⭐⭐⭐ (5/5)

The passing test suite gives me high confidence that the core scheduling, sorting, filtering, recurrence, and conflict detection features work correctly for the tested scenarios.
## 📐 Smarter Scheduling

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | `sort_tasks_by_priority()`, `sort_by_time()` | Sorts tasks by priority and scheduled time. |
| Filtering | `filter_by_completion()`, `filter_by_pet()` | Filters tasks by completion status or pet name. |
| Conflict handling | `detect_conflicts()` | Detects tasks scheduled for the same exact time. |
| Recurring tasks | `create_next_occurrence()`, `complete_task_and_recur()` | Creates the next daily or weekly task after completion. |

## ✨ Features

PawPal+ includes the following features:

- Owner and pet information entry through the Streamlit UI.
- Pet care task creation with duration and priority.
- Priority-based daily schedule generation.
- Sorting tasks by scheduled time.
- Filtering tasks by completion status and pet name.
- Conflict warnings when two tasks share the same scheduled time.
- Daily and weekly recurring task support.
- Automated pytest coverage for the main scheduling behaviors.


## 📸 Demo Walkthrough

1. **Enter the pet owner information.**  
   Type the owner's name into the **Owner Name** field. The application creates an `Owner` object and stores it in the Streamlit session so it persists throughout the session.

2. **Enter the pet information.**  
   Provide the pet's name and select its species. When the first task is added, the application creates a `Pet` object and associates it with the owner.

3. **Add pet care tasks with different durations and priorities.**  
   Enter a task title, specify its duration, and select a priority level (Low, Medium, or High). Repeat this step to add multiple care activities.

4. **Click "Add Task".**  
   Each task is converted into a `Task` object, linked to the selected pet, and displayed in the **Current Tasks** table. A success message confirms that the task has been added.

5. **Click "Generate Schedule".**  
   The scheduler retrieves all tasks, sorts them by priority, applies the available-time constraint, and generates a daily schedule. The output displays the selected tasks in priority order.

6. **Review the scheduling results.**  
   The application displays:
   - A prioritized daily schedule based on available time.
   - A table of tasks sorted by their current time values.
   - A list of incomplete tasks.
   - Conflict warnings when tasks share the same time value.

   Tasks created through the current Streamlit interface use the default time value of `Anytime`. The command-line demonstration in `main.py` uses specific scheduled times to demonstrate time sorting and conflict detection.

7. **Run `python main.py`.**  
   The command-line demonstration executes the scheduling logic outside the Streamlit interface. The terminal displays the generated schedule, recurring task behavior, and any detected scheduling conflicts.

8. **Run `python -m pytest`.**  
   The automated test suite executes all unit tests. The terminal reports the number of collected tests and confirms successful execution with output similar to:

   ```text
   collected 7 items

   tests/test_pawpal.py .......

   ==================== 7 passed ====================
   ```

   This verifies that task completion, sorting, filtering, recurring task creation, conflict detection, and schedule generation all behave as expected.

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->

## Link To a Demo
https://drive.google.com/file/d/13do3sgf8sUv7sO56CkXmySw5chukUQW9/view?usp=sharing
