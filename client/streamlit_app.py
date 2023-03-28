import pandas as pd
import streamlit as st
import requests
import plotly.express as px
import plotly.graph_objects as go
import base64
from pathlib import Path
import streamlit_authenticator as stauth
from yaml.loader import SafeLoader
import yaml
from streamlit_option_menu import option_menu
from datetime import datetime
import pymongo
import pymongo
import requests
import pandas as pd
from bson.json_util import dumps
import json
import plotly.graph_objs as go
import pycountry_convert as pc
import pycountry
from st_pages import Page, show_pages, add_page_title

# Specify what pages should be shown in the sidebar, and what their titles and icons
# should be
show_pages(
    [
        Page("streamlit_app.py", "Dashboard", "🏠"),
        Page("other_pages/articles.py", "Articles", ":books:"),
        Page("other_pages/transactions.py", "Transactions", ":bar_chart:"),
        Page("other_pages/customers.py", "Customers", ":busts_in_silhouette:"),
    ]
)
  # Set the page layout to wide
st.image("hm-symbol-logo.png", width=100)

st.markdown(f"""<h1 style='text-align: center;'>H&M Data - Dashboard</h1>""", unsafe_allow_html=True)

api_key = "secret"
api_base_url = "http://127.0.0.1:8000/api/"
headers = {"X-API-KEY": api_key}
headers = {"Content-Type": "application/json"}

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

# Fetch data
articles_df = fetch_data("articles")
customers_df = fetch_data("customers")
transactions_df = fetch_data("transactions")

    # Instructions
st.write("""
    Our new and improved dashboard app provides you with valuable insights into your retail data through a streamlined interface. The app has three main pages: Articles, Customers, and Transactions. Each page contains visualizations and key performance indicators (KPIs) that help you better understand your business.

    1. **Articles Page:** This page displays KPIs and visualizations related to the best-selling products and departments, as well as the percentage of Ladieswear and Menswear. You can filter articles by department and color using the sidebar.

    2. **Customers Page:** On this page, you'll find KPIs such as customer count, average age, active customer count, and total countries. Additionally, you can view a choropleth map of customers by country and a table of customer data.

    3. **Transactions Page:** This page presents KPIs for total revenue, total transactions, and average transaction value. You can also view visualizations of product type distribution, transactions by sales channel, and total sales by day, along with transaction data in table format.
""")



