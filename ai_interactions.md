# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF7)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.
## Agent Workflow (SF7)

> Document your experience using an AI agent to make multi-step changes autonomously.

**What task did you give the agent?**

I asked the AI coding assistant to extend the PawPal+ scheduling system with a new algorithmic capability that could identify the next available time slot based on the existing scheduled tasks.

**What did the agent do?**

The AI coding assistant helped me plan and implement the next-available-slot feature. It suggested adding scheduling logic to the `Scheduler` class in `pawpal_system.py` and updating `main.py` to demonstrate the new capability through CLI output. The implementation examined the scheduled task times and returned a recommended available time. I then ran `python main.py` to verify the output and `python -m pytest` to confirm that the existing functionality still worked correctly.

**What did you have to verify or fix manually?**

I manually reviewed the suggested code to ensure that it matched my existing `Task` and `Scheduler` class design. I verified the CLI output and confirmed that the scheduler recommended `10:00` as the next available time. I also reran the complete automated test suite and confirmed that all 7 tests passed. This human review ensured that the new stretch feature did not break the existing scheduling, sorting, filtering, recurrence, or conflict detection functionality.


---

## Prompt Comparison (SF11)

> Compare two different prompts (or two different models) on the same task.

|## Prompt Comparison (SF11)

> Compare two different prompts (or two different models) on the same task.

| | Option A | Option B |
|-|----------|----------|
| **Model / tool used** | ChatGPT | Claude |
| **Prompt** | Design a `find_next_available_slot()` algorithm that finds the next available time after considering existing scheduled tasks. Keep the solution simple, readable, and appropriate for a beginner-level Python project. | Design a `find_next_available_slot()` algorithm that finds the next available time after considering existing scheduled tasks. Keep the solution simple, readable, and appropriate for a beginner-level Python project. |
| **Response summary** | See ChatGPT suggestion below. | See Claude suggestion below. |
| **What was useful** | The solution was simple, readable, and compatible with the existing PawPal+ classes. | The solution could identify available gaps between tasks and provided a more advanced scheduling approach. |
| **Problems noticed** | The algorithm does not search for unused gaps between scheduled tasks. | The solution introduced a different class structure and additional complexity that would require significant changes to the existing PawPal+ design. |
| **Decision** | Selected and adapted for the final implementation. | Not selected because the additional complexity and class changes were unnecessary for the current project requirements. |

### ChatGPT Suggestion

ChatGPT suggested filtering out tasks scheduled as `Anytime`, sorting the remaining tasks by scheduled time, and calculating each task's end time using `datetime` and `timedelta`. The algorithm returns the latest ending time as the next available slot.

The main advantage of the ChatGPT solution was its simplicity and compatibility with the existing PawPal+ implementation. The method could be added directly to the existing `Scheduler` class without changing the structure of the `Task`, `Pet`, or `Owner` classes.

One limitation was that the algorithm does not search for unused gaps between scheduled tasks. Instead, it recommends an available time after considering the ending times of the scheduled tasks.

### Claude Suggestion

Claude suggested sorting tasks by start time and using a moving `candidate_start` value to search for available gaps before and between scheduled tasks. If a gap is large enough for the requested task duration, the algorithm returns that time. If no suitable gap exists, it returns a time after the final scheduled task.

The main advantage of Claude's solution was its ability to identify unused time gaps between existing tasks. Claude also explained the algorithm's time complexity and possible future extensions.

One limitation was that Claude's solution introduced a different `Task` and `Scheduler` structure and required an additional `duration_minutes` argument. Adopting the complete solution would require more changes to the existing PawPal+ system.

**Which approach did you use in your final implementation and why?**

I selected and adapted the ChatGPT-assisted approach for my final implementation because it was simple, readable, and compatible with my existing `Task` and `Scheduler` classes. Although Claude's approach provided more advanced gap detection, it introduced additional complexity and would have required changes to the existing system design. The ChatGPT-assisted approach satisfied the stretch feature requirement while preserving the readability and structure of PawPal+.




