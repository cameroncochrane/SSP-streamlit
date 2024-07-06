import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot_member_data(type):

    if type == 'sale_per_order':
        dataframe = pd.read_csv('data/average_sale_member.csv')
        dataframe.set_index(dataframe.columns[0], inplace=True)

        categories = dataframe.columns
        member_data = dataframe.loc['Member'].values
        non_member_data = dataframe.loc['Non-member'].values

        # Define the positions for the bars
        bar_width = 0.35
        index = np.arange(len(categories))

        # Create the bar chart
        fig, ax = plt.subplots()
        member_bar = ax.bar(index, member_data, bar_width, label='Member', color='green')
        non_member_bar = ax.bar(index + bar_width, non_member_data, bar_width, label='Non-member', color='yellow')

        # Add labels, title, and legend

        ax.set_ylabel('Sale Amount($)')
        ax.set_title('Average Sale per Order by Member')
        ax.set_xticks(index + bar_width / 2)
        ax.set_xticklabels(categories)
        ax.set_ylim(300,350)
        ax.legend()
            
    if type == 'sales':
        dataframe = pd.read_csv('data/sales_member.csv')
        dataframe.set_index(dataframe.columns[0], inplace=True)

        categories = dataframe.columns
        member_data = dataframe.loc['Member'].values
        non_member_data = dataframe.loc['Non-member'].values

        # Define the positions for the bars
        bar_width = 0.35
        index = np.arange(len(categories))

        # Create the bar chart
        fig, ax = plt.subplots()
        member_bar = ax.bar(index, member_data, bar_width, label='Member', color='green')
        non_member_bar = ax.bar(index + bar_width, non_member_data, bar_width, label='Non-member', color='yellow')

        # Add labels, title, and legend

        ax.set_ylabel('Sales($)')
        ax.set_title('Total Sales by Member')
        ax.set_xticks(index + bar_width / 2)
        ax.set_xticklabels(categories)
        ax.set_ylim(50000,58000)
        ax.legend()

    if type == 'orders':
        dataframe = pd.read_csv('data/orders_member.csv')
        dataframe.set_index(dataframe.columns[0], inplace=True)

        categories = dataframe.columns
        member_data = dataframe.loc['Member'].values
        non_member_data = dataframe.loc['Non-member'].values

        # Define the positions for the bars
        bar_width = 0.35
        index = np.arange(len(categories))

        # Create the bar chart
        fig, ax = plt.subplots()
        member_bar = ax.bar(index, member_data, bar_width, label='Member', color='green')
        non_member_bar = ax.bar(index + bar_width, non_member_data, bar_width, label='Non-member', color='yellow')

        # Add labels, title, and legend

        ax.set_ylabel('Orders')
        ax.set_title('Total Orders by Member')
        ax.set_xticks(index + bar_width / 2)
        ax.set_xticklabels(categories)
        ax.set_ylim(150,180)
        ax.legend()

    return fig, dataframe

def plot_gender_data(type):

    if type == 'sale_per_order':
        dataframe = pd.read_csv('data/average_sale_gender.csv')
        dataframe.set_index(dataframe.columns[0], inplace=True)

        categories = dataframe.columns
        male_data = dataframe.loc['Male'].values
        female_data = dataframe.loc['Female'].values

        # Define the positions for the bars
        bar_width = 0.35
        index = np.arange(len(categories))

        # Create the bar chart
        fig, ax = plt.subplots()
        male_bar = ax.bar(index, male_data, bar_width, label='Male', color='blue')
        female_bar = ax.bar(index + bar_width, female_data, bar_width, label='Female', color='pink')

        # Add labels, title, and legend

        ax.set_ylabel('Sale Amount($)')
        ax.set_title('Average Sale per Order by Gender')
        ax.set_xticks(index + bar_width / 2)
        ax.set_xticklabels(categories)
        ax.set_ylim(280,350)
        ax.legend()

    if type == 'sales':
        dataframe = pd.read_csv('data/sales_gender.csv')
        dataframe.set_index(dataframe.columns[0], inplace=True)

        categories = dataframe.columns
        male_data = dataframe.loc['Male'].values
        female_data = dataframe.loc['Female'].values

        # Define the positions for the bars
        bar_width = 0.35
        index = np.arange(len(categories))

        # Create the bar chart
        fig, ax = plt.subplots()
        male_bar = ax.bar(index, male_data, bar_width, label='Male', color='blue')
        female_bar = ax.bar(index + bar_width, female_data, bar_width, label='Female', color='pink')

        # Add labels, title, and legend

        ax.set_ylabel('Sales($)')
        ax.set_title('Sales by Gender')
        ax.set_xticks(index + bar_width / 2)
        ax.set_xticklabels(categories)
        ax.set_ylim(40000,65000)
        ax.legend()

    if type == 'orders':
        dataframe = pd.read_csv('data/orders_gender.csv')
        dataframe.set_index(dataframe.columns[0], inplace=True)

        categories = dataframe.columns
        male_data = dataframe.loc['Male'].values
        female_data = dataframe.loc['Female'].values

        # Define the positions for the bars
        bar_width = 0.35
        index = np.arange(len(categories))

        # Create the bar chart
        fig, ax = plt.subplots()
        male_bar = ax.bar(index, male_data, bar_width, label='Male', color='blue')
        female_bar = ax.bar(index + bar_width, female_data, bar_width, label='Female', color='pink')

        # Add labels, title, and legend

        ax.set_ylabel('Orders')
        ax.set_title('Orders by Gender')
        ax.set_xticks(index + bar_width / 2)
        ax.set_xticklabels(categories)
        ax.set_ylim(125,200)
        ax.legend()

    return fig, dataframe

def plot_product_data(type):

    if type == 'sale_per_order':
        dataframe = pd.read_csv('data/average_sales_per_order_product.csv')
        dataframe.set_index(dataframe.columns[0], inplace=True)

        categories = dataframe.index
        mandalay_data = dataframe['Mandalay'].values
        naypyitaw_data = dataframe['Naypyitaw'].values
        yangon_data = dataframe['Yangon'].values


        # Define the positions for the bars
        bar_width = 0.1
        index = np.arange(len(categories))

        # Create the bar chart
        fig, ax = plt.subplots()
        mandalay_bar = ax.bar(index, mandalay_data, bar_width, label='Mandalay', color='red')
        naypyitaw_bar = ax.bar(index + bar_width, naypyitaw_data, bar_width, label='Naypyitaw', color='green')
        yangon_bar = ax.bar(index + bar_width + bar_width, yangon_data, bar_width, label='Yangon', color='blue')


        # Add labels, title, and legend

        ax.set_ylabel('Sale Amount($)')
        ax.set_title('Average Sale Per Order by Product Category')
        ax.set_xticks(index + bar_width / 2)
        ax.set_xticklabels(categories,rotation=40)
        ax.set_ylim(250,380)
        ax.legend()
    
    if type == 'sales':
        dataframe = pd.read_csv('data/sales_product.csv')
        dataframe.set_index(dataframe.columns[0], inplace=True)

        categories = dataframe.index
        mandalay_data = dataframe['Mandalay'].values
        naypyitaw_data = dataframe['Naypyitaw'].values
        yangon_data = dataframe['Yangon'].values


        # Define the positions for the bars
        bar_width = 0.1
        index = np.arange(len(categories))

        # Create the bar chart
        fig, ax = plt.subplots()
        mandalay_bar = ax.bar(index, mandalay_data, bar_width, label='Mandalay', color='red')
        naypyitaw_bar = ax.bar(index + bar_width, naypyitaw_data, bar_width, label='Naypyitaw', color='green')
        yangon_bar = ax.bar(index + bar_width + bar_width, yangon_data, bar_width, label='Yangon', color='blue')


        # Add labels, title, and legend

        ax.set_ylabel('Sales($)')
        ax.set_title('Total Sales by Product Category')
        ax.set_xticks(index + bar_width / 2)
        ax.set_xticklabels(categories,rotation=40)
        ax.set_ylim(10000,25000)
        ax.legend()

    if type == 'orders':
        dataframe = pd.read_csv('data/orders_product.csv')
        dataframe.set_index(dataframe.columns[0], inplace=True)

        categories = dataframe.index
        mandalay_data = dataframe['Mandalay'].values
        naypyitaw_data = dataframe['Naypyitaw'].values
        yangon_data = dataframe['Yangon'].values


        # Define the positions for the bars
        bar_width = 0.1
        index = np.arange(len(categories))

        # Create the bar chart
        fig, ax = plt.subplots()
        mandalay_bar = ax.bar(index, mandalay_data, bar_width, label='Mandalay', color='red')
        naypyitaw_bar = ax.bar(index + bar_width, naypyitaw_data, bar_width, label='Naypyitaw', color='green')
        yangon_bar = ax.bar(index + bar_width + bar_width, yangon_data, bar_width, label='Yangon', color='blue')


        # Add labels, title, and legend

        ax.set_ylabel('Orders')
        ax.set_title('Total Orders by Product Category')
        ax.set_xticks(index + bar_width / 2)
        ax.set_xticklabels(categories,rotation=40)
        ax.set_ylim(40,70)
        ax.legend()

    return fig, dataframe



 