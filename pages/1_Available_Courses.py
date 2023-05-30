import streamlit as st
from sqlalchemy import text
from utils.database import *
import pandas as pd
def create_metrics():
    col1,col2 = st.columns(2)
    query1 = text("SELECT COUNT(*) AS TOTALCOURSES FROM Course")
    query2 = text("SELECT COUNT(DISTINCT Type) AS TOTALTYPES FROM Course")

    result1 = execute_query(st.session_state['connection'],query1)
    courses = [dict(zip(result1.keys(), row)) for row in result1]

    result2 = execute_query(st.session_state['connection'],query2)
    types = [dict(zip(result2.keys(), row)) for row in result2]

    with col1:
        col1.metric("Courses:", courses[0]['TOTALCOURSES'])
    with col2:
        col2.metric("Types:",types[0]['TOTALTYPES'])
def show_lessons(type,max_min_levels):
    with st.expander("Lessons available",expanded=False):
        query = text(f"SELECT Name,Day,StartTime,Duration, GymRoom FROM Schedule, Course WHERE Schedule.CId = Course.CId AND"
                     f" Type = '{type}' AND Level >= {max_min_levels[0]} AND Level <= {max_min_levels[1]}")
        data = execute_query(st.session_state['connection'],query)
        df = pd.DataFrame(data,columns=("Name","Day","StartTime","Duration","Room"))
        st.dataframe(df,use_container_width=True)







def create_show_courses():
    col1,col2 = st.columns(2)
    query1 = text("SELECT DISTINCT Type FROM Course")
    query2 = text("SELECT MAX(Level) AS MaxLevel, MIN(Level) as MinLevel FROM Course")

    result1 = execute_query(st.session_state['connection'],query1)
    result2 = execute_query(st.session_state['connection'],query2)
    types = []
    for row in result1.mappings():
        types.append(row['Type'])
    levels = [dict(zip(result2.keys(), row)) for row in result2]
    with col1:
        type_selected = col1.selectbox("Type of Course",types)
    with col2:
        interval_levels = col2.slider("Select the level range:",levels[0]['MinLevel'],levels[0]['MaxLevel'],(levels[0]['MinLevel'],levels[0]['MaxLevel']))
        query2 = text(f"SELECT Name,Type,Level FROM Course WHERE Type = '{type_selected}' AND Level >= {interval_levels[0]} AND Level <= {interval_levels[1]}")
        data = execute_query(st.session_state['connection'],query2)
    st.subheader("Course :red[Selected]")
    df = pd.DataFrame(data,columns=("Name","Type","Level"))
    if df.empty:
        st.warning("No courses found")
    else:
        st.dataframe(df,use_container_width=True)
        show_lessons(type_selected,interval_levels)

if __name__ == "__main__":
    st.title("Available :red[Courses]")
    if(check_connection()):
        create_metrics()
        create_show_courses()
