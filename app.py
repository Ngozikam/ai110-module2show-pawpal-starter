import streamlit as st

from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

st.subheader("Quick Demo Inputs (UI only)")

owner_name = st.text_input("Owner name", value="Jordan")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])

# Create the Owner only once per session
if "owner" not in st.session_state:
    st.session_state.owner = Owner(
        name=owner_name,
        preferences="Prioritize pet health."
    )

# Update the owner's name if the text box changes
st.session_state.owner.name = owner_name

st.markdown("### Tasks")
st.caption("Add a few tasks. In your final version, these should feed into your scheduler.")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

col1, col2, col3 = st.columns(3)

with col1:
    task_title = st.text_input("Task title", value="Morning walk")

with col2:
    duration = st.number_input(
        "Duration (minutes)",
        min_value=1,
        max_value=240,
        value=20
    )

with col3:
    priority = st.selectbox(
        "Priority",
        ["low", "medium", "high"],
        index=2
    )

if st.button("Add task"):

    # Create the pet if it doesn't exist
    if "pet" not in st.session_state:
        pet = Pet(
            name=pet_name,
            species=species,
            breed="Unknown",
            age=1
        )

        st.session_state.pet = pet
        st.session_state.owner.add_pet(pet)

    else:
        # Update existing pet information
        st.session_state.pet.name = pet_name
        st.session_state.pet.species = species

    # Convert priority text into numbers
    priority_map = {
        "low": 1,
        "medium": 3,
        "high": 5,
    }

    task = Task(
        name=task_title,
        category="General",
        duration_minutes=int(duration),
        priority=priority_map[priority],
    )

    st.session_state.pet.add_task(task)

    st.session_state.tasks.append(
        {
            "title": task.name,
            "duration_minutes": task.duration_minutes,
            "priority": priority,
        }
    )

    st.success("Task added successfully.")

if st.session_state.tasks:
    st.write("Current tasks:")
    st.table(st.session_state.tasks)
else:
    st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Build Schedule")

if st.button("Generate schedule"):

    scheduler = Scheduler(available_minutes=75)

    for task in st.session_state.owner.get_all_tasks():
        scheduler.add_task(task)

    plan = scheduler.generate_daily_plan()
    conflicts = scheduler.detect_conflicts()

    st.success("Today's Schedule")

    for task in plan:
        st.write(
            f"• {task.name} ({task.duration_minutes} min) "
            f"- Priority {task.priority}"
        )

    if conflicts:
        st.warning("Conflicts Detected")
        for conflict in conflicts:
            st.write(conflict)
    else:
        st.success("No scheduling conflicts detected.")