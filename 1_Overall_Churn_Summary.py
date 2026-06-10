import streamlit as st

st.title("Page Working")
import pandas as pd
import plotly.express as px

st.title("📊 Overall Churn Summary")

# Load dataset
df = pd.read_csv("European_Bank.csv")

# KPI calculations
total_customers = len(df)

churned_customers = len(
    df[df['Exited'] == 1]
)

retained_customers = len(
    df[df['Exited'] == 0]
)

churn_rate = (
    df['Exited'].mean()
) * 100

# KPI cards
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Customers",
        total_customers
    )

with col2:
    st.metric(
        "Churned Customers",
        churned_customers
    )

with col3:
    st.metric(
        "Retained Customers",
        retained_customers
    )

with col4:
    st.metric(
        "Churn Rate",
        f"{churn_rate:.2f}%"
    )

# Churn chart
fig = px.histogram(
    df,
    x="Exited",
    color="Exited",
    title="Customer Churn Distribution"
)

st.plotly_chart(
    fig,
    use_container_width=True
)