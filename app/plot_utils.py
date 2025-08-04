import streamlit as st
import matplotlib.pyplot as plt

def render_dashboard(df):
    st.line_chart(df.set_index('date')['PnL'])
    st.write(df.describe())
