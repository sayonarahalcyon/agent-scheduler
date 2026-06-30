import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import json

st.set_page_config(layout="wide")
st.title("🕵️‍♂️ Agent Shift Scheduler")

# --- DATA AUTOMATION FROM SHEET ---
@st.cache_data
def load_initial_shifts_from_sheet():
    try:
        # Read the uploaded CSV data sheet
        df = pd.read_csv("Attendance CST.xlsx - CST.csv")
        
        # Standardize the column headers to match our grid
        day_mapping = {
            'Monday': 'Monday', 'Tuesday': 'Tuesday', 'Wednesday': 'Wednesday',
            'Thursday': 'Thursday', 'Friday': 'Friday', 'Saturday': 'Saturday', 'Sunday': 'Sunday'
        }
        
        # Find the time column (usually the first column)
        time_col = df.columns[0]
        
        # Forward fill the time values since rows stack underneath the hour label
        df[time_col] = df[time_col].ffill()
        
        parsed_shifts = []
        id_counter = 1
        
        # Map sheet times (e.g. "02:00:00") to our display times (e.g. "2:00 AM")
        for index, row in df.iterrows():
            raw_time = str(row[time_col]).strip()
            if not raw_time or raw_time == "nan":
                continue
                
            # Convert HH:MM:SS to H:MM AM/PM format
            try:
                hour_part = int(raw_time.split(":")[0])
                if hour_part == 0:
                    grid_time = "12:00 AM"
                elif hour_part == 12:
                    grid_time = "12:00 PM"
                elif hour_part > 12:
                    grid_time = f"{hour_part - 12}:00 PM"
                else:
                    grid_time = f"{hour_part}:00 AM"
            except:
                continue # Skip if time parsing fails
                
            # Loop through each day column to grab agent names
            for col in df.columns[1:]:
                if col in day_mapping:
                    agent_name = str(row[col]).strip()
                    # Only add if it's a real name and not empty/placeholder numbers
                    if agent_name and agent_name != "nan" and not agent_name.replace(".","",1).isdigit():
                        parsed_shifts.append({
                            "id": f"s{id_counter}",
                            "name": agent_name.upper(),
                            "day": day_mapping[col],
                            "time": grid_time
                        })
                        id_counter += 1
        return parsed_shifts
    except Exception as e:
        # Fallback if file isn't committed to the repo yet
        return [
            {"id": "s1", "name": "ALEX", "day": "Monday", "time": "2:00 AM"}
        ]

# Initialize Shift Data from Sheet
if 'shifts' not in st.session_state:
    st.session_state.shifts = load_initial_shifts_from_sheet()

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
            new_id = f"s{len(st.session_state.shifts) + 1}"
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
