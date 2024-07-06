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

def product_analysis():
    st.title("Supermarket Sales Data Analysis: Product Analysis")
    sales_graph = cf.plot_product_data(type='sales')
    st.pyplot(fig=sales_graph,use_container_width=True)

def gender_analysis():
    st.title("Supermarket Sales Data Analysis: Gender Analysis")

def member_analysis():
    st.title("Supermarket Sales Data Analysis: Member Analysis")

#Sidebar:
with st.sidebar:
    selected = option_menu(
        menu_title="Menu",
        options=["Home", "Product Analysis", "Gender Analysis", "Member Analysis"],
        icons=["house"],
        menu_icon="list",
        default_index=0
    )

#Main:
if selected == "Home":
    home()

if selected == "Product Analysis":
    product_analysis()

if selected == "Gender Analysis":
    gender_analysis()

if selected == "Member Analysis":
    member_analysis()