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
        sales_member = pd.read_csv('data/sales_member.csv')
        sales_member.set_index(sales_member.columns[0], inplace=True)

        categories = sales_member.columns
        member_data = sales_member.loc['Member'].values
        non_member_data = sales_member.loc['Non-member'].values

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
        orders_member = pd.read_csv('data/orders_member.csv')
        orders_member.set_index(orders_member.columns[0], inplace=True)

        categories = orders_member.columns
        member_data = orders_member.loc['Member'].values
        non_member_data = orders_member.loc['Non-member'].values

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
        average_sale_gender = pd.read_csv('data/average_sale_gender.csv')
        average_sale_gender.set_index(average_sale_gender.columns[0], inplace=True)

        categories = average_sale_gender.columns
        male_data = average_sale_gender.loc['Male'].values
        female_data = average_sale_gender.loc['Female'].values

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
        sales_gender = pd.read_csv('data/sales_gender.csv')
        sales_gender.set_index(sales_gender.columns[0], inplace=True)

        categories = sales_gender.columns
        male_data = sales_gender.loc['Male'].values
        female_data = sales_gender.loc['Female'].values

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
        orders_gender = pd.read_csv('data/orders_gender.csv')
        orders_gender.set_index(orders_gender.columns[0], inplace=True)

        categories = orders_gender.columns
        male_data = orders_gender.loc['Male'].values
        female_data = orders_gender.loc['Female'].values

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

    return fig

def plot_product_data(type):

    if type == 'sale_per_order':
        average_sale_per_order_product = pd.read_csv('data/average_sales_per_order_product.csv')
        average_sale_per_order_product.set_index(average_sale_per_order_product.columns[0], inplace=True)

        categories = average_sale_per_order_product.index
        mandalay_data = average_sale_per_order_product['Mandalay'].values
        naypyitaw_data = average_sale_per_order_product['Naypyitaw'].values
        yangon_data = average_sale_per_order_product['Yangon'].values


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
        sales_product = pd.read_csv('data/sales_product.csv')
        sales_product.set_index(sales_product.columns[0], inplace=True)

        categories = sales_product.index
        mandalay_data = sales_product['Mandalay'].values
        naypyitaw_data = sales_product['Naypyitaw'].values
        yangon_data = sales_product['Yangon'].values


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
        orders_product = pd.read_csv('data/orders_product.csv')
        orders_product.set_index(orders_product.columns[0], inplace=True)

        categories = orders_product.index
        mandalay_data = orders_product['Mandalay'].values
        naypyitaw_data = orders_product['Naypyitaw'].values
        yangon_data = orders_product['Yangon'].values


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

    return fig



 