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

st.markdown("<h1 style='text-align: center;'>H&M Data - Dashboard</h1>", unsafe_allow_html=True)


api_key = "secret"
api_base_url = "http://127.0.0.1:8000/api/"

headers = {"X-API-KEY": api_key}

def fetch_data(endpoint, params=None):
    api_url = f"http://127.0.0.1:8000/api/{endpoint}"
    response = requests.get(api_url, headers=headers, params=params)
    
    if response.status_code == 200:
        try:
            data = response.json()
            column_names = data['columns']
            data_dicts = data['data']
            return pd.DataFrame(data_dicts, columns=column_names)
        except Exception as e:
            print("Error parsing JSON data:", e)
            return pd.DataFrame()
    else:
        print(f"Error fetching data from API, status code: {response.status_code}, response content: {response.content}")
        return pd.DataFrame()


articles_df = fetch_data("articles")

print(articles_df.head())




