import streamlit as st

st.set_page_config(
    page_title="Customer Churn Analytics",
    page_icon="🏦",
    layout="wide"
)

st.title("🏦 Customer Segmentation & Churn Pattern Analytics")

st.markdown("""
### European Banking Customer Churn Dashboard

This dashboard analyzes customer churn patterns in European banking.

### Project Objectives
- Measure overall churn rate
- Analyze geography-wise churn
- Compare age & tenure churn
- Explore high-value customer churn

Use the sidebar to navigate between pages.
""")

st.success("Dashboard Loaded Successfully")