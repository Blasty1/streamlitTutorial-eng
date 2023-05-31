import streamlit as st
from sqlalchemy import text
from utils.database import *
import pandas as pd

def create_widgets():
    col1,col2 = st.columns(2)
    with col1:
        surname = col1.text_input("Type instructor's surname")
    with col2:
        dates = execute_query(st.session_state['connection'],text("SELECT MIN(DateOfBirth) AS minDate , MAX(DateOfBirth) AS maxDate FROM Trainer"))
        date_max_min = [dict(zip(dates.keys(), row)) for row in dates] #to create a structure
        date = col2.date_input("Select the data range of instructor's birthday",value=(date_max_min[0]['minDate'],date_max_min[0]['maxDate']),min_value=date_max_min[0]['minDate'],max_value=date_max_min[0]['maxDate'])

    query = text(f"SELECT * FROM Trainer WHERE Surname LIKE '%{surname}%' AND DateOfBirth >= '{date[0]}' AND DateOfBirth <= '{date[1]}'")
    results = execute_query(st.session_state['connection'],query)
    df = pd.DataFrame(results,columns=("SSN","Name","Surname","Date Of Birth","Email","Phone Number"))

    if df.empty:
        st.warning("No data found.", icon='⚠️')
    else:
        for index, row in df.iterrows():
            st.dataframe(row,use_container_width=True)

if __name__ == "__main__":
    st.title("Available :red[Instructors]")
    if check_connection():
        create_widgets()
