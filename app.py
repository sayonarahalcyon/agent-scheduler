import streamlit as st
import streamlit.components.v1 as components
import json

st.set_page_config(layout="wide")
st.title("🕵️‍♂️ Agent Shift Scheduler")
st.subheader("Drag and drop agent blocks to adjust their shifts")

# 1. Initialize Sample Shift Data in temporary memory
if 'shifts' not in st.session_state:
    st.session_state.shifts = [
        {"id": "s1", "name": "ALEX", "day": "Monday", "time": "2:00 AM"},
        {"id": "s2", "name": "SAM", "day": "Monday", "time": "9:00 AM"},
        {"id": "s3", "name": "SARAH", "day": "Monday", "time": "6:00 PM"},
        {"id": "s4", "name": "CHLOE", "day": "Friday", "time": "6:00 PM"},
        {"id": "s5", "name": "BEN", "day": "Saturday", "time": "11:00 PM"}
    ]

# 2. Define Time Slots and Days for our grid
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
hours = ["12:00 AM"] + [f"{i}:00 AM" for i in range(1, 12)] + ["12:00 PM"] + [f"{i}:00 PM" for i in range(1, 12)]
