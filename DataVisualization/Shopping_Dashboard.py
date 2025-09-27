import streamlit as st
import pandas as pd

st.title("Shopping Trends Dashboard")
data = pd.read_csv('../data/shopping_trends_updated.csv')

st.header("Data Overview")
st.dataframe(data.sample(5))


st.header("Gender Distribution")
st.bar_chart(data['Gender'].value_counts())
