import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title="Data Visualization Demo", page_icon="📊")

st.title("Data Visualization Demo 📊")

# Generate sample data
np.random.seed(42)
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)

# Display different types of charts
st.subheader("Line Chart")
st.line_chart(chart_data)

st.subheader("Area Chart")
st.area_chart(chart_data)

st.subheader("Bar Chart")
st.bar_chart(chart_data)

# Display the raw data
st.subheader("Raw Data")
st.dataframe(chart_data)