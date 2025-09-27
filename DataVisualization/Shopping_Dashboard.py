import streamlit as st
import pandas as pd

st.title("Shopping Trends Dashboard")
data = pd.read_csv('../data/shopping_trends_updated.csv')

st.header("Data Overview")
st.dataframe(data.sample(5))


graph_list = st.selectbox(
    "Select Graph Type",
    ("Gender Distribution", "Category Distribution", "Top 10 Products by Sales")
)
st.sidebar.markdown("### Other Pages")
with st.sidebar:
    st.page_link("Shopping_Dashboard.py", label="Home", icon="🏠")
    st.page_link("pages/data_description.py", label="Data Description", icon="📄")
    
st.sidebar.header("Filters")
with st.sidebar:
    age_filter = st.slider("Select Age Range", data['Age'].min(), data['Age'].max(), (20, 50))
    filtered_data = data[(data['Age'] >= age_filter[0]) & (data['Age'] <= age_filter[1])]


if graph_list == "Gender Distribution":
    st.header("Gender Distribution")
    st.bar_chart(filtered_data['Gender'].value_counts())
elif graph_list == "Category Distribution":
    st.header("Category Distribution")
    st.bar_chart(filtered_data['Category'].value_counts())
elif graph_list == "Top 10 Products by Sales":
    st.header("Top 10 Products by Sales")
    st.bar_chart(filtered_data['Item Purchased'].value_counts().sort_values(ascending=False).head(10), horizontal=True)

