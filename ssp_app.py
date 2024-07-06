#Base modules:
import pandas as pd
import numpy as np

import streamlit as st
from streamlit_option_menu import option_menu
import streamlit_shadcn_ui as ui
import streamlit.components.v1 as components

#Custom modules:
import chart_functions as cf

#Functions:
def home():
    st.title("Supermarket Sales Data Analysis")
    st.write("This dashboard app features the full analysis of the supermarket sales data.")
    st.write("Navigate the app using the pages menu on the left.")

def store_analysis():
    st.title("Supermarket Sales Data Analysis: Store Analysis")

    #Sales:
    sales_graph, dataframe_sales = cf.plot_store_data(type='sales')

    st.dataframe(dataframe_sales,use_container_width=True)

    st.title(":red[Sales]")
    st.pyplot(fig=sales_graph,use_container_width=True)
    #Orders:
    st.title(":red[Orders]")
    orders_graph, dataframe_orders = cf.plot_store_data(type='orders')

    st.pyplot(fig=orders_graph,use_container_width=True)

    #Sale per Order:
    st.title(":red[Average Sale Per Order]")
    aso_graph, dataframe_aso = cf.plot_store_data(type='sale_per_order')

    st.pyplot(fig=aso_graph,use_container_width=True)

def product_analysis():
    st.title("Supermarket Sales Data Analysis: Product Analysis")

    #Sales:
    st.title(":red[Product Analysis: Sales]")
    sales_graph, dataframe_sales = cf.plot_product_data(type='sales')

    st.pyplot(fig=sales_graph,use_container_width=True)
    st.dataframe(dataframe_sales,use_container_width=True)

    #Orders:
    st.title(":red[Product Analysis: Orders]")
    orders_graph, dataframe_orders = cf.plot_product_data(type='orders')

    st.pyplot(fig=orders_graph,use_container_width=True)
    st.dataframe(dataframe_orders,use_container_width=True)

    #Sale per Order:
    st.title(":red[Product Analysis: Average Sale Per Order]")
    aso_graph, dataframe_aso = cf.plot_product_data(type='sale_per_order')

    st.pyplot(fig=aso_graph,use_container_width=True)
    st.dataframe(dataframe_aso,use_container_width=True)

def gender_analysis():
    st.title("Supermarket Sales Data Analysis: Gender Analysis")

    #Sales:
    st.title(":red[Gender Analysis: Sales]")
    sales_graph, dataframe_sales = cf.plot_gender_data(type='sales')

    st.pyplot(fig=sales_graph,use_container_width=True)
    st.dataframe(dataframe_sales,use_container_width=True)
    
    #Orders:
    st.title(":red[Gender Analysis: Orders]")
    orders_graph, dataframe_orders = cf.plot_gender_data(type='orders')

    st.pyplot(fig=orders_graph,use_container_width=True)
    st.dataframe(dataframe_orders,use_container_width=True)

    #Sale per Order:
    st.title(":red[Gender Analysis: Average Sale per Order]")
    aso_graph, dataframe_aso = cf.plot_gender_data(type='sale_per_order')

    st.pyplot(fig=aso_graph,use_container_width=True)
    st.dataframe(dataframe_aso,use_container_width=True)

def member_analysis():
    st.title("Supermarket Sales Data Analysis: Member Analysis")

    #Sales:
    st.title(":red[Member Analysis: Sales]")
    sales_graph, dataframe_sales = cf.plot_member_data(type='sales')

    st.pyplot(fig=sales_graph,use_container_width=True)
    st.dataframe(dataframe_sales,use_container_width=True)
    
    #Orders:
    st.title(":red[Member Analysis: Orders]")
    orders_graph, dataframe_orders = cf.plot_member_data(type='orders')

    st.pyplot(fig=orders_graph,use_container_width=True)
    st.dataframe(dataframe_orders,use_container_width=True)
    
    #Sale per Order:
    st.title(":red[Member Analysis: Average Sale per Order]")
    aso_graph, dataframe_aso = cf.plot_member_data(type='sale_per_order')

    st.pyplot(fig=aso_graph,use_container_width=True)
    st.dataframe(dataframe_aso,use_container_width=True)
    


#Sidebar:
with st.sidebar:
    selected = option_menu(
        menu_title="Menu",
        options=["Home", "Store Analysis","Product Analysis", "Gender Analysis", "Member Analysis"],
        icons=["house"],
        menu_icon="list",
        default_index=0
    )

#Main:
if selected == "Home":
    home()

if selected == "Store Analysis":
    store_analysis()

if selected == "Product Analysis":
    product_analysis()

if selected == "Gender Analysis":
    gender_analysis()

if selected == "Member Analysis":
    member_analysis()

