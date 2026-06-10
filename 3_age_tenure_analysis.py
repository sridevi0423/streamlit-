import streamlit as st

st.title("Page Working")
import pandas as pd
import plotly.express as px

st.title("👥 Age & Tenure Analysis")

# Load dataset
df = pd.read_csv(
    "European_Bank.csv"
)

# Create age groups
df['AgeGroup'] = pd.cut(
    df['Age'],
    bins=[18, 30, 45, 60, 100],
    labels=[
        'Young',
        'Adult',
        'Middle Age',
        'Senior'
    ],
    include_lowest=True
)

# Create tenure groups
df['TenureGroup'] = pd.cut(
    df['Tenure'],
    bins=[-1, 3, 7, 10],
    labels=[
        'New',
        'Mid-Term',
        'Long-Term'
    ]
)

# Age churn
age_churn = (
    df.groupby(
        'AgeGroup'
    )['Exited']
    .mean()
    .reset_index()
)

age_churn['Exited'] = (
    age_churn['Exited'] * 100
)

fig1 = px.bar(
    age_churn,
    x='AgeGroup',
    y='Exited',
    title='Age Group Churn Rate (%)',
    text_auto=True
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# Tenure churn
tenure_churn = (
    df.groupby(
        'TenureGroup'
    )['Exited']
    .mean()
    .reset_index()
)

tenure_churn['Exited'] = (
    tenure_churn['Exited'] * 100
)

fig2 = px.bar(
    tenure_churn,
    x='TenureGroup',
    y='Exited',
    title='Tenure Group Churn Rate (%)',
    text_auto=True
)

st.plotly_chart(
    fig2,
    use_container_width=True
)