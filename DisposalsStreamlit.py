
""" from pip._internal import main as pipmain

pipmain(['install', "streamlit"])
pipmain(['install', "plotly"]) """


import streamlit as st
import pandas as pd
import plotly.express as px

# Title for the app
st.title('Hawthorn Player Disposals')

# Load the data
@st.cache_data
def load_data():
    data = pd.read_csv('Hawthorn.csv')
    data['DI'] = pd.to_numeric(data['DI'], errors='coerce')  # Ensure DI is numeric
    return data

df = load_data()

# Create the plot with customizations
fig = px.bar(df, x='Player', y='DI', title='Disposals by Player',
             color_discrete_sequence=['#636EFA', '#EF553B', '#00CC96'])

# Updating the layout
fig.update_layout(
    xaxis_title='Player',
    yaxis_title='Disposals',
    width=800,   # Width of the chart
    height=600,  # Height of the chart
    font=dict(size=12),  # Font size for labels and titles
    title_font_size=20   # Font size for the main title
)

# Adding hover data
fig.update_traces(hoverinfo='y+name', marker=dict(line=dict(width=2, color='DarkSlateGrey')))

# Show the plot
st.plotly_chart(fig)

