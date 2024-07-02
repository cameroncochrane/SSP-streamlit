#Base modules:
import pandas as pd
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu
import streamlit_shadcn_ui as ui

#Custom modules:
import chart_functions as cf


#Functions:

def home():
    st.title("Supermarket Sales Data Analysis")
    st.write("This dashboard app features the full analysis of the supermarket sales data.")
    st.write("Navigate the app using the pages menu on the left.")

def shadcn_button():
    trigger_button = ui.button(text='This is a button')
    return trigger_button

home()
button = shadcn_button()
