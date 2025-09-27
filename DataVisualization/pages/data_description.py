import streamlit as st

st.sidebar.markdown("### Other Pages")
with st.sidebar:
    st.page_link("Shopping_Dashboard.py", label="Home", icon="🏠")
    st.page_link("pages/data_description.py", label="Data Description", icon="📄")

st.title("Data Description")
st.markdown("""
This dashboard provides insights into shopping trends based on various demographic factors. Users can filter data by age
and visualize distributions of gender, product categories, and top products by sales.
The dataset used contains information on customer purchases, including age, gender, category of items purchased, and
the specific items bought.""")