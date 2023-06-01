import streamlit as st
from sqlalchemy import text
from utils.database import *
import pandas as pd

def create_form():
    col1,col2 = st.columns(2)
    error ,completed = False, False
    messages = []
    with col1:
        code = col1.text_input("Course's Code").strip()
        type = col1.text_input("Course's Type").strip()



    with col2:
        name = col2.text_input("Course's Name").strip()
        level = col2.number_input("Course's Level",step=1,min_value=1,max_value=4)

    clicked = st.button("Create new course!",use_container_width=True,type="primary")
    if clicked:
        query = text("SELECT CId FROM Course")
        results = execute_query(st.session_state['connection'],query)
        existing_codes = []

        messages.clear() #to reset errors
        error = False
        completed = False

        for row in results.mappings():
            existing_codes.append(row['CId'].lower())
        if name == '':
            error = True
            messages.append('Name missing')
        if code.lower() in existing_codes:
            error = True
            messages.append('Code just presents')
        if code == '':
            error = True
            messages.append('Code missing')
        if type == '':
            error = True
            messages.append('Type missing')
        if  level < 0 or level > 4:
            error = True
            messages.append('Level must be among 0 and 4')

        if(not error):
            query = text(f"INSERT INTO Course(CId,Name,Type,Level) VALUES('{code}','{name}','{type}',{level})")
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
        st.success("Course created")
if __name__ == "__main__":
    st.title("New :red[Course]")
    if check_connection():
        create_form()
