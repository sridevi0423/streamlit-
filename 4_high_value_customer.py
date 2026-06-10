import streamlit as st

st.title("Page Working")
import pandas as pd
import plotly.express as px

st.title(
    "💰 High Value Customer Churn"
)

# Load dataset
df = pd.read_csv(
    "European_Bank.csv"
)

# High-value customers
high_value = df[
    df['Balance']
    >
    df['Balance']
    .median()
]

# KPI
high_churn = (
    high_value[
        'Exited'
    ].mean()
) * 100

st.metric(
    "High Value Churn Ratio",
    f"{high_churn:.2f}%"
)

# Churn chart
fig1 = px.histogram(
    high_value,
    x='Exited',
    color='Exited',
    title='High Value Customer Churn'
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# Engagement chart
engagement = (
    df.groupby(
        'IsActiveMember'
    )['Exited']
    .mean()
    .reset_index()
)

engagement['Exited'] = (
    engagement['Exited']
    * 100
)

fig2 = px.bar(
    engagement,
    x='IsActiveMember',
    y='Exited',
    title='Engagement Drop Indicator',
    text_auto=True
)

st.plotly_chart(
    fig2,
    use_container_width=True
)