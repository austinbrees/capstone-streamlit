import streamlit as st
import requests
import pandas as pd
import plotly.graph_objects as go
import json
import plotly.express as px

st.image("hm-symbol-logo.png", width=100)


st.subheader('Articles')

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

articles_df = fetch_data("articles")
transactions_df = fetch_data("transactions")

merged_df = pd.merge(transactions_df, articles_df, on='article_id', how='inner')




# Display merged data table
# Calculating KPIs
total_transactions = merged_df["t_dat"].nunique()
total_products = merged_df["article_id"].nunique()

# Number of unique customers
unique_customers = merged_df["customer_id"].nunique()

# Best-selling department
best_selling_dept = merged_df.groupby("product_group_name")["price"].sum().reset_index().sort_values("price", ascending=False).iloc[0]["product_group_name"]

# Best-selling product
best_selling_product = merged_df.groupby("prod_name")["price"].sum().reset_index().sort_values("price", ascending=False).iloc[0]["prod_name"]
total_products = merged_df["article_id"].nunique()
Ladieswear = merged_df[merged_df.index_group_name == 'Ladieswear']
perc_Ladieswear = (Ladieswear['article_id'].nunique() / total_products) * 100

menswear = merged_df[merged_df.index_group_name == 'Menswear']
perc_menswear = (menswear['article_id'].nunique() / total_products) * 100

# Display best selling department
st.subheader(f"Best-selling department: {best_selling_dept}")

# Display best selling product
st.subheader(f"Best-selling product: {best_selling_product}")

kpi10, kpi11, kpi12 = st.columns(3)


#Displaying KPIS
    # Displaying KPIS
kpi10.metric (
    label="Number of unique products",
    value=total_products,
    delta="updated automatically"
    )

kpi11.metric(
    label = "Ladieswear",
    value = str(round(perc_Ladieswear, 1)) + '%',
    delta = perc_Ladieswear,
    )

kpi12.metric(
    label = "Menswear",
    value = str(round(perc_menswear, 1)) + '%',
    delta = perc_menswear,
    )

# Sidebar for selecting filters
st.sidebar.subheader("Filter articles by:")
selected_department = st.sidebar.selectbox("Department", merged_df["index_group_name"].unique())
selected_colour = st.sidebar.selectbox("Colour", merged_df["perceived_colour_value_name"].unique())




department_options = merged_df['department_name'].unique()

# Define sidebar filters
department = st.sidebar.selectbox('Product', department_options)

# Filter the merged dataframe by selected department
filtered_df = merged_df[merged_df['index_group_name'] == selected_department]

# Create a histogram of sales
fig = px.histogram(filtered_df, x='prod_name', y='price', nbins=20, 
                   title=f'Sales of {selected_department} products',
                   labels={'prod_name': 'Product Name', 'price': 'Price'})

# Show the histogram
st.plotly_chart(fig)

