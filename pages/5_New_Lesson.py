from datetime import time

import streamlit as st
from sqlalchemy import text
from utils.database import *
import pandas as pd
def create_layout():
    col1,col2 = st.columns(2)
    error ,completed = False, False
    messages = []
    with col1:
        query1 = text('SELECT SSN FROM Trainer')
        results_ssn = execute_query(st.session_state['connection'],query1)

        query2 = text("SELECT CId FROM Course")
        results_course = execute_query(st.session_state['connection'],query2)

        existing_ssns = []
        existing_courses = []

        for row in results_ssn.mappings():
            existing_ssns.append(row['SSN'])

        for row in results_course.mappings():
            existing_courses.append(row['CId'])

        ssn_selected = col1.selectbox("Instructor",existing_ssns)
        course_selected = col1.selectbox("Course",existing_courses)
        start_time = col1.slider('Start Time',value=time(10,00))



    with col2:
        days = [
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday'
        ]
        gym_room = col2.text_input("Gym Room").strip()
        duration = col2.slider("Duration",step=1,value=40,min_value=1,max_value=60)
        day = col2.selectbox("Day of the Week",days)

    clicked=st.button("Create Lesson",use_container_width=True,type="primary")
    if clicked:
        error = False
        completed = False
        messages.clear()

        if(gym_room == ''):
            error = True
            messages.append("No gym room specified")

        query = text(f"SELECT COUNT(*) AS SameDay FROM Schedule WHERE Day = '{day}' AND CId = '{course_selected}'")
        results = execute_query(st.session_state['connection'],query)
        SameDaySameCourse = [dict(zip(results.keys(), row)) for row in results]
        if SameDaySameCourse[0]['SameDay'] != 0:
            error = True
            messages.append("The same course is just organized in the same day")

        query = text(f"SELECT COUNT(*) AS Occupied FROM Schedule WHERE Day = '{day}' AND StartTime = '{start_time}' AND SSN = '{ssn_selected}'")
        results = execute_query(st.session_state['connection'],query)
        trainerBusy = [dict(zip(results.keys(), row)) for row in results]

        if trainerBusy[0]['Occupied'] != 0:
            error = True
            messages.append("Instructor occupied for that combination of Day and Time")

        if(not error):
                query = text(f"INSERT INTO Schedule(SSN,Day,StartTime,Duration,GymRoom,CId) VALUES('{ssn_selected}','{day}','{start_time}',{duration},'{gym_room}','{course_selected}')")
                try:
                    execute_query(st.session_state['connection'],query)
                    st.session_state['connection'].commit()
                    completed = True
                except Exception as e:
                    error = True
                    messages.append(e)
    if error:
        for message in messages:
            st.error(message)

    if completed:
        st.success("Lesson created")


if __name__ == "__main__":
    st.title("New :red[Lesson]")
    if check_connection():
        create_layout()
