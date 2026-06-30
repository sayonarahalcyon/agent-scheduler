import streamlit as st
import streamlit.components.v1 as components
import json

st.set_page_config(layout="wide")
st.title("🕵️‍♂️ Agent Shift Scheduler")

# --- EMBEDDED SHEET DATA ---
# This holds your exact schedule directly in code so no file upload is needed!
if 'shifts' not in st.session_state:
    st.session_state.shifts = [
        # 12:00 AM
        {"id": "e1", "name": "JOJO", "day": "Monday", "time": "12:00 AM"},
        {"id": "e2", "name": "NOREEN", "day": "Monday", "time": "12:00 AM"},
        {"id": "e3", "name": "JULY", "day": "Monday", "time": "12:00 AM"},
        {"id": "e4", "name": "JOJO", "day": "Tuesday", "time": "12:00 AM"},
        {"id": "e5", "name": "NOREEN", "day": "Tuesday", "time": "12:00 AM"},
        {"id": "e6", "name": "JOJO", "day": "Wednesday", "time": "12:00 AM"},
        {"id": "e7", "name": "NOREEN", "day": "Wednesday", "time": "12:00 AM"},
        {"id": "e8", "name": "JULY", "day": "Wednesday", "time": "12:00 AM"},
        {"id": "e9", "name": "JOJO", "day": "Thursday", "time": "12:00 AM"},
        {"id": "e10", "name": "NOREEN", "day": "Thursday", "time": "12:00 AM"},
        {"id": "e11", "name": "NOREEN", "day": "Friday", "time": "12:00 AM"},
        {"id": "e12", "name": "JULY", "day": "Friday", "time": "12:00 AM"},
        {"id": "e13", "name": "JOJO", "day": "Saturday", "time": "12:00 AM"},
        {"id": "e14", "name": "NOREEN", "day": "Saturday", "time": "12:00 AM"},
        {"id": "e15", "name": "ELIZABETH", "day": "Saturday", "time": "12:00 AM"},
        {"id": "e16", "name": "JULY", "day": "Saturday", "time": "12:00 AM"},
        {"id": "e17", "name": "JOJO", "day": "Sunday", "time": "12:00 AM"},
        {"id": "e18", "name": "NOREEN", "day": "Sunday", "time": "12:00 AM"},
        {"id": "e19", "name": "JULY", "day": "Sunday", "time": "12:00 AM"},

        # 1:00 AM
        {"id": "e20", "name": "JOJO", "day": "Monday", "time": "1:00 AM"},
        {"id": "e21", "name": "NOREEN", "day": "Monday", "time": "1:00 AM"},
        {"id": "e22", "name": "JULY", "day": "Monday", "time": "1:00 AM"},
        {"id": "e23", "name": "JOJO", "day": "Tuesday", "time": "1:00 AM"},
        {"id": "e24", "name": "NOREEN", "day": "Tuesday", "time": "1:00 AM"},
        {"id": "e25", "name": "JOJO", "day": "Wednesday", "time": "1:00 AM"},
        {"id": "e26", "name": "NOREEN", "day": "Wednesday", "time": "1:00 AM"},
        {"id": "e27", "name": "JULY", "day": "Wednesday", "time": "1:00 AM"},
        {"id": "e28", "name": "JOJO", "day": "Thursday", "time": "1:00 AM"},
        {"id": "e29", "name": "NOREEN", "day": "Thursday", "time": "1:00 AM"},
        {"id": "e30", "name": "NOREEN", "day": "Friday", "time": "1:00 AM"},
        {"id": "e31", "name": "JULY", "day": "Friday", "time": "1:00 AM"},
        {"id": "e32", "name": "JOJO", "day": "Saturday", "time": "1:00 AM"},
        {"id": "e33", "name": "NOREEN", "day": "Saturday", "time": "1:00 AM"},
        {"id": "e34", "name": "ELIZABETH", "day": "Saturday", "time": "1:00 AM"},
        {"id": "e35", "name": "JULY", "day": "Saturday", "time": "1:00 AM"},
        {"id": "e36", "name": "JOJO", "day": "Sunday", "time": "1:00 AM"},
        {"id": "e37", "name": "NOREEN", "day": "Sunday", "time": "1:00 AM"},
        {"id": "e38", "name": "JULY", "day": "Sunday", "time": "1:00 AM"},

        # 2:00 AM
        {"id": "e39", "name": "STELLA", "day": "Monday", "time": "2:00 AM"},
        {"id": "e40", "name": "MARK", "day": "Monday", "time": "2:00 AM"},
        {"id": "e41", "name": "NOREEN", "day": "Monday", "time": "2:00 AM"},
        {"id": "e42", "name": "JULY", "day": "Monday", "time": "2:00 AM"},
        {"id": "e43", "name": "STELLA", "day": "Tuesday", "time": "2:00 AM"},
        {"id": "e44", "name": "MARK", "day": "Tuesday", "time": "2:00 AM"},
        {"id": "e45", "name": "NOREEN", "day": "Tuesday", "time": "2:00 AM"},
        {"id": "e46", "name": "STELLA", "day": "Wednesday", "time": "2:00 AM"},
        {"id": "e47", "name": "JULY", "day": "Wednesday", "time": "2:00 AM"},
        {"id": "e48", "name": "STELLA", "day": "Thursday", "time": "2:00 AM"},
        {"id": "e49", "name": "MARK", "day": "Thursday", "time": "2:00 AM"},
        {"id": "e50", "name": "NOREEN", "day": "Thursday", "time": "2:00 AM"},
        {"id": "e51", "name": "STELLA", "day": "Friday", "time": "2:00 AM"},
        {"id": "e52", "name": "MARK", "day": "Friday", "time": "2:00 AM"},
        {"id": "e53", "name": "NOREEN", "day": "Friday", "time": "2:00 AM"},
        {"id": "e54", "name": "JULY", "day": "Friday", "time": "2:00 AM"},
        {"id": "e55", "name": "NOREEN", "day": "Saturday", "time": "2:00 AM"},
        {"id": "e56", "name": "ELIZABETH", "day": "Saturday", "time": "2:00 AM"},
        {"id": "e57", "name": "JULY", "day": "Saturday", "time": "2:00 AM"},
        {"id": "e58", "name": "MARK", "day": "Saturday", "time": "2:00 AM"},
        {"id": "e59", "name": "MARK", "day": "Sunday", "time": "2:00 AM"},
        {"id": "e60", "name": "NOREEN", "day": "Sunday", "time": "2:00 AM"},
        {"id": "e61", "name": "JULY", "day": "Sunday", "time": "2:00 AM"},

        # 3:00 AM
        {"id": "e62", "name": "STELLA", "day": "Monday", "time": "3:00 AM"},
        {"id": "e63", "name": "MARK", "day": "Monday", "time": "3:00 AM"},
        {"id": "e64", "name": "NOREEN", "day": "Monday", "time": "3:00 AM"},
        {"id": "e65", "name": "MICHELL", "day": "Monday", "time": "3:00 AM"},
        {"id": "e66", "name": "JULY", "day": "Monday", "time": "3:00 AM"},
        {"id": "e67", "name": "STELLA", "day": "Tuesday", "time": "3:00 AM"},
        {"id": "e68", "name": "MARK", "day": "Tuesday", "time": "3:00 AM"},
        {"id": "e69", "name": "NOREEN", "day": "Tuesday", "time": "3:00 AM"},
        {"id": "e70", "name": "MICHELL", "day": "Tuesday", "time": "3:00 AM"},
        {"id": "e71", "name": "STELLA", "day": "Wednesday", "time": "3:00 AM"},
        {"id": "e72", "name": "MICHELL", "day": "Wednesday", "time": "3:00 AM"},
        {"id": "e73", "name": "JULY", "day": "Wednesday", "time": "3:00 AM"},
        {"id": "e74", "name": "STELLA", "day": "Thursday", "time": "3:00 AM"},
        {"id": "e75", "name": "MARK", "day": "Thursday", "time": "3:00 AM"},
        {"id": "e76", "name": "NOREEN", "day": "Thursday", "time": "3:00 AM"},
        {"id": "e77", "name": "JULY", "day": "Thursday", "time": "3:00 AM"},
        {"id": "e78", "name": "STELLA", "day": "Friday", "time": "3:00 AM"},
        {"id": "e79", "name": "MARK", "day": "Friday", "time": "3:00 AM"},
        {"id": "e80", "name": "NOREEN", "day": "Friday", "time": "3:00 AM"},
        {"id": "e81", "name": "MICHELL", "day": "Friday", "time": "3:00 AM"},
        {"id": "e82", "name": "JULY", "day": "Friday", "time": "3:00 AM"},
        {"id": "e83", "name": "NOREEN", "day": "Saturday", "time": "3:00 AM"},
        {"id": "e84", "name": "ELIZABETH", "day": "Saturday", "time": "3:00 AM"},
        {"id": "e85", "name": "MICHELL", "day": "Saturday", "time": "3:00 AM"},
        {"id": "e86", "name": "JULY", "day": "Saturday", "time": "3:00 AM"},
        {"id": "e87", "name": "MARK", "day": "Saturday", "time": "3:00 AM"},
        {"id": "e88", "name": "MARK", "day": "Sunday", "time": "3:00 AM"},
        {"id": "e89", "name": "NOREEN", "day": "Sunday", "time": "3:00 AM"},
        {"id": "e90", "name": "MICHELL", "day": "Sunday", "time": "3:00 AM"},
        {"id": "e91", "name": "JULY", "day": "Sunday", "time": "3:00 AM"},

        # 4:00 AM
        {"id": "e92", "name": "STELLA", "day": "Monday", "time": "4:00 AM"},
        {"id": "e93", "name": "STELLA", "day": "Tuesday", "time": "4:00 AM"},
        {"id": "e94", "name": "STELLA", "day": "Wednesday", "time": "4:00 AM"},
        {"id": "e95", "name": "STELLA", "day": "Thursday", "time": "4:00 AM"},
        {"id": "e96", "name": "STELLA", "day": "Friday", "time": "4:00 AM"},
        {"id": "e97", "name": "ELIZABETH", "day": "Saturday", "time": "4:00 AM"},
        {"id": "e98", "name": "MARK", "day": "Sunday", "time": "4:00 AM"},

        # 6:00 PM (18:00:00)
        {"id": "e99", "name": "JOJO", "day": "Monday", "time": "6:00 PM"},
        {"id": "e100", "name": "RENCE", "day": "Monday", "time": "6:00 PM"},
        {"id": "e101", "name": "JOHN", "day": "Monday", "time": "6:00 PM"},
        {"id": "e102", "name": "HENNA", "day": "Monday", "time": "6:00 PM"},
        {"id": "e103", "name": "PETTER", "day": "Monday", "time": "6:00 PM"},
        {"id": "e104", "name": "YARI", "day": "Monday", "time": "6:00 PM"},
        {"id": "e105", "name": "JOJO", "day": "Tuesday", "time": "6:00 PM"},
        {"id": "e106", "name": "RENCE", "day": "Tuesday", "time": "6:00 PM"},
        {"id": "e107", "name": "AGA", "day": "Tuesday", "time": "6:00 PM"},
        {"id": "e108", "name": "HENNA", "day": "Tuesday", "time": "6:00 PM"},
        {"id": "e109", "name": "YARI", "day": "Tuesday", "time": "6:00 PM"},
        {"id": "e110", "name": "ELLA", "day": "Tuesday", "time": "6:00 PM"},
        {"id": "e111", "name": "JOJO", "day": "Wednesday", "time": "6:00 PM"},
        {"id": "e112", "name": "RENCE", "day": "Wednesday", "time": "6:00 PM"},
        {"id": "e113", "name": "HENNA", "day": "Wednesday", "time": "6:00 PM"},
        {"id": "e114", "name": "ELLA", "day": "Wednesday", "time": "6:00 PM"},
        {"id": "e115", "name": "YARI", "day": "Wednesday", "time": "6:00 PM"},
        {"id": "e116", "name": "JOHN", "day": "Wednesday", "time": "6:00 PM"},
        {"id": "e117", "name": "PETTER", "day": "Wednesday", "time": "6:00 PM"},
        {"id": "e118", "name": "AGA", "day": "Wednesday", "time": "6:00 PM"},
        {"id": "e119", "name": "JOHN", "day": "Thursday", "time": "6:00 PM"},
        {"id": "e120", "name": "HENNA", "day": "Thursday", "time": "6:00 PM"},
        {"id": "e121", "name": "PETTER", "day": "Thursday", "time": "6:00 PM"},
        {"id": "e122", "name": "ELLA", "day": "Thursday", "time": "6:00 PM"},
        {"id": "e123", "name": "YARI", "day": "Thursday", "time": "6:00 PM"},
        {"id": "e124", "name": "AGA", "day": "Thursday", "time": "6:00 PM"},
        {"id": "e125", "name": "AGA", "day": "Friday", "time": "6:00 PM"},
        {"id": "e126", "name": "JOHN", "day": "Friday", "time": "6:00 PM"},
        {"id": "e127", "name": "HENNA", "day": "Friday", "time": "6:00 PM"},
        {"id": "e128", "name": "PETTER", "day": "Friday", "time": "6:00 PM"},
        {"id": "e129", "name": "ELLA", "day": "Friday", "time": "6:00 PM"},
        {"id": "e130", "name": "JOJO", "day": "Friday", "time": "6:00 PM"},
        {"id": "e131", "name": "RENCE", "day": "Friday", "time": "6:00 PM"},
        {"id": "e132", "name": "JOJO", "day": "Saturday", "time": "6:00 PM"},
        {"id": "e133", "name": "RENCE", "day": "Saturday", "time": "6:00 PM"},
        {"id": "e134", "name": "AGA", "day": "Saturday", "time": "6:00 PM"},
        {"id": "e135", "name": "JOHN", "day": "Saturday", "time": "6:00 PM"},
        {"id": "e136", "name": "PETTER", "day": "Saturday", "time": "6:00 PM"},
        {"id": "e137", "name": "ELLA", "day": "Saturday", "time": "6:00 PM"},
        {"id": "e138", "name": "YARI", "day": "Saturday", "time": "6:00 PM"},
        {"id": "e139", "name": "JOJO", "day": "Sunday", "time": "6:00 PM"},
        {"id": "e140", "name": "RENCE", "day": "Sunday", "time": "6:00 PM"},
        {"id": "e141", "name": "JOHN", "day": "Sunday", "time": "6:00 PM"},
        {"id": "e142", "name": "PETTER", "day": "Sunday", "time": "6:00 PM"},
        {"id": "e143", "name": "ELLA", "day": "Sunday", "time": "6:00 PM"},
        {"id": "e144", "name": "YARI", "day": "Sunday", "time": "6:00 PM"},
        {"id": "e145", "name": "HENNA", "day": "Sunday", "time": "6:00 PM"},

        # 7:00 PM (19:00:00)
        {"id": "e146", "name": "JOJO", "day": "Monday", "time": "7:00 PM"},
        {"id": "e147", "name": "RENCE", "day": "Monday", "time": "7:00 PM"},
        {"id": "e148", "name": "JOHN", "day": "Monday", "time": "7:00 PM"},
        {"id": "e149", "name": "HENNA", "day": "Monday", "time": "7:00 PM"},
        {"id": "e150", "name": "YARI", "day": "Monday", "time": "7:00 PM"},
        {"id": "e151", "name": "JOJO", "day": "Tuesday", "time": "7:00 PM"},
        {"id": "e152", "name": "RENCE", "day": "Tuesday", "time": "7:00 PM"},
        {"id": "e153", "name": "AGA", "day": "Tuesday", "time": "7:00 PM"},
        {"id": "e154", "name": "HENNA", "day": "Tuesday", "time": "7:00 PM"},
        {"id": "e155", "name": "YARI", "day": "Tuesday", "time": "7:00 PM"},
        {"id": "e156", "name": "JOJO", "day": "Wednesday", "time": "7:00 PM"},
        {"id": "e157", "name": "RENCE", "day": "Wednesday", "time": "7:00 PM"},
        {"id": "e158", "name": "HENNA", "day": "Wednesday", "time": "7:00 PM"},
        {"id": "e159", "name": "YARI", "day": "Wednesday", "time": "7:00 PM"},
        {"id": "e160", "name": "JOHN", "day": "Wednesday", "time": "7:00 PM"},
        {"id": "e161", "name": "AGA", "day": "Wednesday", "time": "7:00 PM"},
        {"id": "e162", "name": "JOHN", "day": "Thursday", "time": "7:00 PM"},
        {"id": "e163", "name": "HENNA", "day": "Thursday", "time": "7:00 PM"},
        {"id": "e164", "name": "YARI", "day": "Thursday", "time": "7:00 PM"},
        {"id": "e165", "name": "AGA", "day": "Thursday", "time": "7:00 PM"},
        {"id": "e166", "name": "AGA", "day": "Friday", "time": "7:00 PM"},
        {"id": "e167", "name": "JOHN", "day": "Friday", "time": "7:00 PM"},
        {"id": "e168", "name": "HENNA", "day": "Friday", "time": "7:00 PM"},
        {"id": "e169", "name": "JOJO", "day": "Friday", "time": "7:00 PM"},
        {"id": "e170", "name": "RENCE", "day": "Friday", "time": "7:00 PM"},
        {"id": "e171", "name": "JOJO", "day": "Saturday", "time": "7:00 PM"},
        {"id": "e172", "name": "RENCE", "day": "Saturday", "time": "7:00 PM"},
        {"id": "e173", "name": "AGA", "day": "Saturday", "time": "7:00 PM"},
        {"id": "e174", "name": "JOHN", "day": "Saturday", "time": "7:00 PM"},
        {"id": "e175", "name": "YARI", "day": "Saturday", "time": "7:00 PM"},
        {"id": "e176", "name": "JOJO", "day": "Sunday", "time": "7:00 PM"},
        {"id": "e177", "name": "RENCE", "day": "Sunday", "time": "7:00 PM"},
        {"id": "e178", "name": "JOHN", "day": "Sunday", "time": "7:00 PM"},
        {"id": "e179", "name": "YARI", "day": "Sunday", "time": "7:00 PM"},
        {"id": "e180", "name": "HENNA", "day": "Sunday", "time": "7:00 PM"},

        # 8:00 PM (20:00:00)
        {"id": "e181", "name": "JOJO", "day": "Monday", "time": "8:00 PM"},
        {"id": "e182", "name": "RENCE", "day": "Monday", "time": "8:00 PM"},
        {"id": "e183", "name": "JOHN", "day": "Monday", "time": "8:00 PM"},
        {"id": "e184", "name": "NOREEN", "day": "Monday", "time": "8:00 PM"},
        {"id": "e185", "name": "JOJO", "day": "Tuesday", "time": "8:00 PM"},
        {"id": "e186", "name": "RENCE", "day": "Tuesday", "time": "8:00 PM"},
        {"id": "e187", "name": "AGA", "day": "Tuesday", "time": "8:00 PM"},
        {"id": "e188", "name": "YARI", "day": "Tuesday", "time": "8:00 PM"},
        {"id": "e189", "name": "JOJO", "day": "Wednesday", "time": "8:00 PM"},
        {"id": "e190", "name": "RENCE", "day": "Wednesday", "time": "8:00 PM"},
        {"id": "e191", "name": "YARI", "day": "Wednesday", "time": "8:00 PM"},
        {"id": "e192", "name": "CHANNIE", "day": "Wednesday", "time": "8:00 PM"},
        {"id": "e193", "name": "JOHN", "day": "Thursday", "time": "8:00 PM"},
        {"id": "e194", "name": "NOREEN", "day": "Thursday", "time": "8:00 PM"},
        {"id": "e195", "name": "YARI", "day": "Thursday", "time": "8:00 PM"},
        {"id": "e196", "name": "CHANNIE", "day": "Thursday", "time": "8:00 PM"},
        {"id": "e197", "name": "AGA", "day": "Friday", "time": "8:00 PM"},
        {"id": "e198", "name": "JOHN", "day": "Friday", "time": "8:00 PM"},
        {"id": "e199", "name": "NOREEN", "day": "Friday", "time": "8:00 PM"},
        {"id": "e200", "name": "CHANNIE", "day": "Friday", "time": "8:00 PM"},
        {"id": "e201", "name": "JOJO", "day": "Saturday", "time": "8:00 PM"},
        {"id": "e202", "name": "RENCE", "day": "Saturday", "time": "8:00 PM"},
        {"id": "e203", "name": "AGA", "day": "Saturday", "time": "8:00 PM"},
        {"id": "e204", "name": "CHANNIE", "day": "Saturday", "time": "8:00 PM"},
        {"id": "e205", "name": "JOJO", "day": "Sunday", "time": "8:00 PM"},
        {"id": "e206", "name": "RENCE", "day": "Sunday", "time": "8:00 PM"},
        {"id": "e207", "name": "JOHN", "day": "Sunday", "time": "8:00 PM"},
        {"id": "e208", "name": "CHANNIE", "day": "Sunday", "time": "8:00 PM"}
    ]

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
hours = ["12:00 AM"] + [f"{i}:00 AM" for i in range(1, 12)] + ["12:00 PM"] + [f"{i}:00 PM" for i in range(1, 12)]

# Panel to add names manually if needed
st.markdown("### ➕ Schedule a New Shift")
col1, col2, col3, col4 = st.columns([2, 2, 2, 1])

with col1:
    new_name = st.text_input("Agent Name", placeholder="e.g. DAVID").upper()
with col2:
    new_day = st.selectbox("Day", days)
with col3:
    new_time = st.selectbox("Start Time", hours)
with col4:
    st.write("")
    st.write("") 
    if st.button("Add Agent Block", use_container_width=True):
        if new_name.strip():
            new_id = f"e{len(st.session_state.shifts) + 1}"
            st.session_state.shifts.append({
                "id": new_id,
                "name": new_name,
                "day": new_day,
                "time": new_time
            })
            st.toast(f"Added {new_name} to the schedule!", icon="➕")
            st.rerun()

st.markdown("---")

# 3. Create the Custom Drag-and-Drop Grid Component (HTML/JS)
html_code = f"""
<!DOCTYPE html>
<html>
<head>
<style>
    body {{ font-family: sans-serif; background-color: #f9f9f9; margin: 0; padding: 10px; }}
    .schedule-grid {{ display: grid; grid-template-columns: 120px repeat(7, 1fr); gap: 6px; background-color: #ddd; padding: 6px; border-radius: 4px; }}
    .header-cell {{ background-color: #333; color: white; text-align: center; padding: 12px; font-weight: bold; font-size: 14px; }}
    .time-cell {{ background-color: #eee; padding: 12px 6px; font-weight: bold; font-size: 12px; text-align: right; border-right: 2px solid #ccc; display: flex; align-items: center; justify-content: flex-end; }}
    
    .drop-zone {{ background-color: white; min-height: 90px; height: auto; padding: 6px; border: 1px dashed #ccc; display: flex; flex-direction: column; gap: 6px; align-items: center; justify-content: flex-start; box-sizing: border-box; }}
    .drop-zone.drag-over {{ background-color: #e0f7fa; border-color: #00acc1; }}
    
    .agent-block {{ background-color: #fff3e0; border: 2px solid #ffb74d; color: #e65100; padding: 6px 4px; border-radius: 4px; cursor: move; font-weight: bold; font-size: 11px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: center; width: 95%; box-sizing: border-box; word-break: break-all; }}
    .agent-block:active {{ opacity: 0.5; }}
</style>
</head>
<body>

<div class="schedule-grid">
    <div class="header-cell">Time</div>
    {"".join([f'<div class="header-cell">{day}</div>' for day in days])}

    <script>
        const days = {json.dumps(days)};
        const hours = {json.dumps(hours)};
        const initialShifts = {json.dumps(st.session_state.shifts)};
        
        hours.forEach(hour => {{
            document.write(`<div class="time-cell">${{hour}}</div>`);
            days.forEach(day => {{
                document.write(`<div class="drop-zone" data-day="${{day}}" data-time="${{hour}}" ondragover="allowDrop(event)" ondragleave="clearDropStyle(event)" ondrop="drop(event)"></div>`);
            }});
        }});

        initialShifts.forEach(shift => {{
            const cell = document.querySelector(`[data-day="${{shift.day}}"][data-time="${{shift.time}}"]`);
            if(cell) {{
                const block = document.createElement('div');
                block.className = 'agent-block';
                block.draggable = true;
                block.id = shift.id;
                block.innerText = shift.name;
                block.setAttribute('ondragstart', 'drag(event)');
                cell.appendChild(block);
            }}
        }});

        function drag(ev) {{
            ev.dataTransfer.setData("text/plain", ev.target.id);
        }}

        function allowDrop(ev) {{
            ev.preventDefault();
            if (ev.currentTarget.classList.contains('drop-zone')) {{
                ev.currentTarget.classList.add('drag-over');
            }}
        }}

        function clearDropStyle(ev) {{
            ev.currentTarget.classList.remove('drag-over');
        }}

        function drop(ev) {{
            ev.preventDefault();
            ev.currentTarget.classList.remove('drag-over');
            const blockId = ev.dataTransfer.getData("text/plain");
            const draggedElement = document.getElementById(blockId);
            
            let targetCell = ev.target;
            if (targetCell.classList.contains('agent-block')) {{
                targetCell = targetCell.parentElement;
            }}
            
            if (targetCell && targetCell.classList.contains('drop-zone')) {{
                targetCell.appendChild(draggedElement);
                
                const targetDay = targetCell.getAttribute('data-day');
                const targetTime = targetCell.getAttribute('data-time');
                
                const updatedShift = {{ id: blockId, day: targetDay, time: targetTime }};
                window.parent.postMessage({{type: 'streamlit:setComponentValue', value: updatedShift}}, '*');
            }}
        }}
    </script>
</div>

</body>
</html>
"""

# 4. Render Grid & Capture Drag Events
component_value = components.html(html_code, height=2500, scrolling=True)

# 5. Process Changes Real-Time in Streamlit Backend
if component_value and isinstance(component_value, dict) and 'id' in component_value:
    for shift in st.session_state.shifts:
        if shift['id'] == component_value['id']:
            if shift['day'] != component_value['day'] or shift['time'] != component_value['time']:
                shift['day'] = component_value['day']
                shift['time'] = component_value['time']
                st.toast(f"Moved {shift['name']} to {component_value['day']} at {component_value['time']}!", icon="✅")
                st.rerun()
