
# **KPI Dashboard**

The KPI Dashboard is a Streamlit web application designed to provide insights into various Key Performance Indicators (KPIs) related to sales transactions, customers, and articles. The application fetches data from an API and visualizes the KPIs using Plotly charts.

Link to site: https://frontend-dot-directed-racer-376415.oa.r.appspot.com/


## **Technologies Used**

- Python: The backend programming language used for data processing and visualization.
- Streamlit: A fast and easy-to-use Python library for building interactive web applications.
- Pandas: A powerful data manipulation and analysis library for Python.
- Plotly: A Python graphing library used for creating interactive and visually appealing charts.
- Requests: A Python library used for making HTTP requests to fetch data from the API.

## **Features**

- Interactive visualizations: The dashboard provides interactive charts built using Plotly, which allows users to hover over data points for more information, zoom in/out, and pan.
- Filters and selection: The application allows users to filter and select data based on various attributes, such as department and colour, using the sidebar.
- Responsive layout: The dashboard has a responsive layout that automatically adjusts to different screen sizes and devices.

## **Table of Contents**

- **[Installation](https://www.notion.so/b3257a3ed20d415d808ce6721d1cd07e)**
- **[Usage](https://www.notion.so/b3257a3ed20d415d808ce6721d1cd07e)**
- **[Pages](https://chat.openai.com/chat?model=gpt-4#pages)**
    - **[Transactions](https://www.notion.so/b3257a3ed20d415d808ce6721d1cd07e)**
    - **[Customers](https://www.notion.so/b3257a3ed20d415d808ce6721d1cd07e)**
    - **[Articles](https://www.notion.so/b3257a3ed20d415d808ce6721d1cd07e)**

## **Installation**

To install the required packages for this project, run the following command:

```
bashCopy code
pip install -r requirements.txt

```

## **Usage**

To run the Streamlit application, use the following command:

```
bashCopy code
streamlit run app.py

```

## **Pages**

### **Transactions**

The Transactions page displays transaction-related KPIs, such as Total Revenue, Total Transactions, and Average Transaction Value. It also provides a bar chart of Product Types Distribution and a bar chart of Transactions by Sales Channel. The transactions data is displayed as a table.

### **Customers**

The Customers page displays customer-related KPIs, such as Customer Count, Average Age, Active Count, and Total Countries. It also provides a choropleth map showing the distribution of customers by country. The customers data is displayed as a table. 

### **Articles**

The Articles page displays article-related KPIs, such as Number of Unique Products, Ladieswear, and Menswear. The best-selling department and best-selling product are displayed as subheaders. The page also provides a histogram of sales by product for the selected department and colour, which can be filtered using the sidebar.

To filter the articles by department or colour, use the sidebar on the right side of the page.

---

This KPI Dashboard provides a comprehensive view of various KPIs related to sales transactions, customers, and articles. It enables users to easily identify trends and patterns in the data and make data-driven decisions. The use of modern technologies and interactive features makes the application user-friendly and engaging.
