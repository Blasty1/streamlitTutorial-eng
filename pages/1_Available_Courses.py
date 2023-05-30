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
if __name__ == "__main__":
    st.title("Available Courses")
    if(check_connection()):
        create_metrics()
