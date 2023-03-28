import streamlit as st
import requests
import pandas as pd
import plotly.graph_objects as go
import json
import plotly.express as px
import matplotlib.pyplot as plt
import altair as alt



st.subheader('Transactions')



api_key = "secret"
api_base_url = "http://127.0.0.1:8000/api/"

headers = {"X-API-KEY": api_key}

def fetch_data(endpoint, params=None):
    api_url = f"http://127.0.0.1:8000/api/{endpoint}"
    response = requests.get(api_url, headers=headers, params=params)
    
    if response.status_code == 200:
        try:
            data_str = response.text
            data_dicts = json.loads(data_str)
            if data_dicts:
                column_names = list(data_dicts[0].keys())
                return pd.DataFrame(data_dicts, columns=column_names)
            else:
                print("Empty data received from API.")
                return pd.DataFrame()
        except Exception as e:
            print("Error parsing JSON data:", e)
            return pd.DataFrame()
    else:
        print(f"Error fetching data from API, status code: {response.status_code}, response content: {response.content}")
        return pd.DataFrame()

transactions_df = fetch_data("transactions")
articles_df = fetch_data("articles")


# Define KPIs
total_revenue = transactions_df['price'].sum()
num_transactions = transactions_df.shape[0]
avg_transaction_value = total_revenue / num_transactions


st.subheader('Transactions KPIs')
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label='Total Revenue', value=f'${total_revenue:,.2f}')
with col2:
    st.metric(label= 'Total Trans.', value=num_transactions)
with col3:
    st.metric(label='Avg. Transaction Value', value=f'${avg_transaction_value:,.2f}')
    
# Display transaction data as table
st.subheader('Transactions')

col4, col5 = st.columns(2)
with col4:
    fig = px.bar(articles_df["product_type_name"].value_counts().reset_index(),
                 x='index', y='product_type_name', labels={'index': 'Product Type', 'product_type_name': 'Count'},
                 title='Product Types Distribution')
    st.plotly_chart(fig)
with col5:
    kpi3 = transactions_df["sales_channel_id"].nunique()
    fig = px.bar(transactions_df["sales_channel_id"].value_counts().reset_index(),
        x='index', y='sales_channel_id', labels={'index': 'Sales Channel', 'sales_channel_id': 'Count'},
        title='Transactions by Sales Channel')
    st.plotly_chart(fig)
    

# First, convert the 't_dat' column to a datetime object
transactions_df['t_dat'] = pd.to_datetime(transactions_df['t_dat'])

# Group by day and sum the sales
daily_sales = transactions_df.groupby('t_dat')['price'].sum().reset_index()

# Sort the data by date
daily_sales = daily_sales.sort_values('t_dat')


st.subheader('Transasctions Data')

st.write(transactions_df)

