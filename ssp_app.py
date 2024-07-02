#Base modules:
import pandas as pd
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu

#Custom modules:
import chart_functions as cf


#Functions:

def home():
    st.title("Supermarket Sales Data Analysis")
    st.write("This dashboard app features the full analysis of the supermarket sales data.")

home()
