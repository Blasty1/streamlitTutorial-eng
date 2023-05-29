import streamlit as st
from sqlalchemy import create_engine,text

"""Collects the main functions shared by the various pages"""
def connect_db():
    try:
        engine = create_engine(f"mysql+pymysql://{st.secrets['MYSQL_USER']}:{st.secrets.MYSQL_PASSWORD}@{st.secrets['HOST']}:3307/{st.secrets['MYSQL_DATABASE']}")
        conn=engine.connect()
        return conn
    except:
        return False

def execute_query(conn,query):
    if(conn):
        return conn.execute(query)
def check_connection():
    if 'connection' not in st.session_state:
        st.session_state['connection'] = False

    if st.sidebar.button("Connect To DB"):
        myconn = connect_db()
        if myconn:
            st.session_state['connection'] =  myconn
        else:
            st.sidebar.error("Error connecting to DB")

    if st.session_state['connection']:
        st.sidebar.success('Connected to DB')
        return True

#Show numbers in a more compact form
def compact_format(num):
    num=float(num)
    if abs(num) >= 1e9:
        return "{:.2f}B".format(num / 1e9)
    elif abs(num) >= 1e6:
        return "{:.2f}M".format(num / 1e6)
    elif abs(num) >= 1e3:
        return "{:.2f}K".format(num / 1e3)
    else:
        return "{:.0f}".format(num)
