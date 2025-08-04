import streamlit as st
from app.data_loader import load_latest_data
from app.plot_utils import render_dashboard

st.title("Algo Trading Analytics Dashboard")

data = load_latest_data()
if data is not None:
    render_dashboard(data)
else:
    st.warning("No data found. Please check sync job.")
