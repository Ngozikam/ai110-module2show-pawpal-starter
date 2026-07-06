# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?
### 1a. Initial Design

### 1a. Initial Design

I designed PawPal+ using four main classes: **Owner**, **Pet**, **Task**, and **Scheduler**.

The **Owner** class stores the pet owner's information and manages one or more pets. The **Pet** class stores pet details and maintains a list of care tasks. The **Task** class represents activities such as feeding, walking, medication, grooming, and enrichment, along with their duration and priority. The **Scheduler** class organizes tasks into a daily care plan by considering priorities and available time. This modular design assigns a single responsibility to each class, making the system easier to maintain and extend.

### Building Blocks

| Class | Key Attributes | Key Methods |
|--------|----------------|-------------|
| Owner | name, preferences, pets | add_pet(), get_pets() |
| Pet | name, species, breed, age, tasks | add_task(), get_tasks() |
| Task | name, duration, priority, completed | mark_complete(), is_high_priority() |
| Scheduler | available_minutes, tasks | sort_tasks_by_priority(), generate_daily_plan() |


**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

### 1b. Design Changes

After reviewing the UML diagram and Python class skeleton with AI assistance, I determined that the overall design already satisfied the project requirements. The AI review suggested considering additional relationships, such as linking the Owner to the Scheduler, and future enhancements such as task validation and conflict checking. However, I chose to keep the design simple because these additions were not required for Phase 1 and would introduce unnecessary complexity. I retained the Task attributes for duration and priority and the Scheduler attribute for available_minutes because they directly support the scheduling requirements described in the project.

### Three Core User Actions

1. Enter owner and pet information.
2. Add or edit pet care tasks with duration and priority.
3. Generate and view a daily care plan based on available time, priority, and constraints.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

The scheduler considers task priority, available time, completion status, pet name, task frequency, and scheduled time. Priority and available time matter most because the daily plan should select the most important tasks that fit into the owner's available schedule.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

One tradeoff my scheduler makes is that it detects conflicts only when two tasks are scheduled for the exact same start time. It does not yet detect overlapping task durations (for example, a task from 09:00–09:30 overlapping one from 09:15–09:45). This approach keeps the implementation simple and efficient while satisfying the current project requirements.
---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

I used AI to brainstorm the class design, generate the Mermaid UML diagram, review my Python skeleton, improve my scheduling logic, and draft test cases. The most helpful prompts were specific prompts that asked for one task at a time, such as how to sort tasks by time, how to detect conflicts, and how to test recurring tasks.

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

One AI suggestion I modified was adding extra relationships between Owner and Scheduler. I decided not to make the design too complex because the Scheduler could retrieve tasks through the Owner's pets when needed. I verified AI suggestions by running `python main.py`, checking the Streamlit UI, and running `python -m pytest`.
---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

I tested task completion, adding tasks to pets, sorting tasks by time, recurring daily tasks, conflict detection, filtering by pet name, and daily plan generation based on available time. These tests were important because they verify the main behavior of the scheduling system.

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

I am highly confident that the scheduler works for the tested scenarios because all seven pytest tests passed. If I had more time, I would test additional edge cases such as overlapping time ranges, invalid task durations, duplicate pet names, and empty schedules.

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

The object-oriented design worked well because each class had a clear responsibility. The CLI-first workflow also helped me verify the backend before connecting it to Streamlit.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

I would improve the UI by allowing the user to enter exact task times, pet ages, breeds, and available daily minutes. I would also improve conflict detection so it can detect overlapping time ranges instead of only exact time matches.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?

My key takeaway is that AI is most useful when I remain the lead architect. AI helped with code suggestions, testing ideas, and documentation, but I still had to review the design, verify the logic, and decide which suggestions fit the project requirements.
