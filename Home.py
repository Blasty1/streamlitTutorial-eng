import streamlit as st
import numpy as np
import pandas as pd
from utils.database import *

st.set_page_config(
    page_title="HomeWork 4",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://dbdmg.polito.it/',
        'Report a bug': "https://dbdmg.polito.it/",
        'About': "# *Introduction to Databases* course"
    }
)
st.title("HomeWork :red[4]")
col1,col2 = st.columns(2)
with col1:
    col1.subheader("🤷 Why?")
    col1.markdown("I'm working at this project to build a web application using a python framework called _streamlit_ in order to complete the professor assignment.")
with col2:
    col2.subheader("🤌 What?")
    col2.write("The web application references to a Gym database built with Docker, the aim is create a enviroment where the users can access to their data through graphics and managing them")
col1,col2 = st.columns(2)
with col1:
    col1.subheader("🪪 Who?")
    col1.write("My full name is Bruno Carchia and i'm at 2 year of university to Politecnico Di Torino. "
               "My github is accessible clicking [here](https://github.com/Blasty1)")
with col2:
    col2.subheader("💻 Project")
    col2.write("In particular, the application handles a gym and its organization, allowing the creation of courses and their management")
check_connection()
st.columns(3)[1].image("./images/gym_logo.png") #to center the image

