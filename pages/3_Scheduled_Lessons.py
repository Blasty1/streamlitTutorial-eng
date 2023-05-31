import streamlit as st
from sqlalchemy import text
from utils.database import *
import pandas as pd

def create_lessonsForTime_tab(tab):
    tab.subheader("Number of lessons for each time slot")
    query = text("SELECT StartTime,COUNT(*) AS NumberOfLessons FROM Schedule GROUP BY StartTime")
    results = execute_query(st.session_state['connection'],query)
    df = pd.DataFrame(results,columns=["Start Time","Number Of Lessons"])
    tab.bar_chart(df,x='Start Time',y='Number Of Lessons')


def create_lessonsForDay_tab(tab):
    tab.subheader("Number of lessons scheduled per day")
    query = text("SELECT Day,COUNT(*) AS NumberOfLessons FROM Schedule GROUP BY Day")
    results = execute_query(st.session_state['connection'],query)
    df = pd.DataFrame(results,columns=["Day","Number Of Lessons"])
    tab.line_chart(df,x='Day',y='Number Of Lessons')

if __name__ == "__main__":
    st.title("Scheduled :red[Lessons]")
    tab1, tab2 = st.tabs(['📊 Each Time','📈 Each Day'])
    if check_connection():
        create_lessonsForTime_tab(tab1)
        create_lessonsForDay_tab(tab2)

