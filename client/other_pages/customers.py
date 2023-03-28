import streamlit as st
import requests
import pandas as pd
import plotly.graph_objects as go
import json
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import base64
from pathlib import Path
import streamlit_authenticator as stauth
from streamlit_option_menu import option_menu
from datetime import datetime
import pymongo
import pymongo
import requests
import pandas as pd
from bson.json_util import dumps
import pycountry_convert as pc
import pycountry

st.image("hm-symbol-logo.png", width=100)


st.subheader('Customers')

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

customers_df = fetch_data("customers")

# Filter out unexpected values in age column
age_col = customers_df['age']
age_col = age_col[(age_col.notnull()) & (age_col != '') & (age_col.apply(lambda x: isinstance(x, (int, float))))]

# Calculate mean age
avg_age = age_col.mean()

# Define KPIs
num_customers = customers_df.shape[0]
num_active_customers = customers_df[customers_df['club_member_status'] == 'ACTIVE'].shape[0]
num_countries = customers_df['country_id'].nunique()

# Display KPIs
st.subheader('Key Performance Indicators')
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label='Cust. Count', value=num_customers)
with col2:
    st.metric(label='Avg. Age', value=f'{avg_age:.1f}')
with col3:
    st.metric(label='Active Count', value=num_active_customers)
with col4:
    st.metric(label='Total Countries', value=num_countries)

# Display customer data as table
st.subheader('Customers by Country')
# Aggregate customers by country
customers_by_country = customers_df.groupby('country_id').size().reset_index(name='customer_count')

# Define function to convert ISO 2 to ISO 3 code
# Define function to convert ISO 2 to ISO 3 code
def iso2_to_iso3(iso2):
    try:
        country = pycountry.countries.get(alpha_2=iso2)
        return country.alpha_3
    except:
        return None
    
# Add ISO 3 column to customers_by_country
customers_by_country['iso3'] = customers_by_country['country_id'].apply(iso2_to_iso3)

# Create a choropleth map
fig = go.Figure(data=go.Choropleth(
    locations=customers_by_country['iso3'],
    z=customers_by_country['customer_count'],
    text=customers_by_country['iso3'],
    colorscale='Viridis',
    autocolorscale=False,
    reversescale=True,
    marker_line_color='darkgray',
    marker_line_width=0.5,
    colorbar_title='Number of Customers',
    ))

fig.update_layout(
    title_text='Customers by Country',
    geo=dict(
        scope='europe',
        showframe=False,
        showcoastlines=False,
        projection_type='equirectangular',
        bgcolor='#0F1117'
    )
)

st.plotly_chart(fig, use_container_width=True)













