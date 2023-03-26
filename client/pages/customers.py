import streamlit as st
import requests
import pandas as pd
import geopandas as gpd
import pydeck as pdk
import json 

st.subheader('Customers')


url = 'http://localhost:5000/api/customers'  # Replace with your API URL
response = requests.get(url)
print("Status code:", response.status_code)
print("Response text:", response.text)


# Convert JSON data to DataFrame
# customers_df = pd.DataFrame(data)


# # Load GeoJSON data for countries
# url = 'https://raw.githubusercontent.com/datasets/geo-countries/master/data/countries.geojson'
# countries_geojson = gpd.read_file(url)

# print(customers_df.head())


# # Merge customers data with countries GeoJSON data
# merged_data = countries_geojson.merge(customers_df, left_on='ISO_A2', right_on='country_id')

# # Calculate some metric for the choropleth map (e.g., count of customers by country)
# metric = merged_data.groupby('country_id').size().reset_index(name='count')

# # Merge the metric back to the GeoJSON data
# merged_data = countries_geojson.merge(metric, left_on='ISO_A2', right_on='country_id')

# # Create the choropleth map
# view_state = pdk.ViewState(latitude=51.1657, longitude=10.4515, zoom=3, pitch=40.5)
# layer = pdk.Layer(
#     'GeoJsonLayer',
#     data=merged_data,
#     opacity=0.8,
#     stroked=False,
#     filled=True,
#     extruded=True,
#     wireframe=True,
#     get_elevation='count * 1000',
#     get_fill_color='[255, count / maxValue * 255, 255, 255]',
#     get_line_color=[255, 255, 255],
#     pickable=True,
#     auto_highlight=True,
# )

# map = pdk.Deck(layers=[layer], initial_view_state=view_state, tooltip={"text": "Country: {NAME}\nCount: {count}"})

# # Render the map in your Streamlit app
# st.title('Choropleth Map')
# st.pydeck_chart(map)
