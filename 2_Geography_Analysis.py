import streamlit as st

st.title("Page Working")
import pandas as pd
import plotly.express as px

st.title("🌍 Geography-wise Churn Analysis")

# Load dataset
df = pd.read_csv(
    "European_Bank.csv"
)

# Sidebar filter
country_filter = st.sidebar.multiselect(
    "Select Country",
    options=df['Geography'].unique(),
    default=df['Geography'].unique()
)

# Filter data
filtered_df = df[
    df['Geography']
    .isin(country_filter)
]

# Geography churn
geo_churn = (
    filtered_df.groupby(
        'Geography'
    )['Exited']
    .mean()
    .reset_index()
)

geo_churn['Exited'] = (
    geo_churn['Exited'] * 100
)

fig1 = px.bar(
    geo_churn,
    x='Geography',
    y='Exited',
    title='Geography-wise Churn Rate (%)',
    text_auto=True
)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# Gender drill-down
fig2 = px.histogram(
    filtered_df,
    x='Geography',
    color='Gender',
    title='Gender Distribution by Geography'
)

st.plotly_chart(
    fig2,
    use_container_width=True
)