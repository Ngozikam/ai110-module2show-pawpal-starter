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

## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. Enter the pet owner information.
2. Add two pets and assign care tasks with different priorities and times.
3. Run `main.py` to generate a daily schedule.
4. View the prioritized schedule and any detected task conflicts.
5. Verify the backend logic by running the automated pytest test suite.

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
