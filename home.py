import streamlit as st
import pandas as pd

st.title("🥨🥨WedSite Developing using Python🥨🥨")
st.header("🥪WedSite Developing using Python🥪")

st.subheader("Thanathip MTV")
st.image('./img/my.jpg')

dt=pd.read_csv('./data/iris-3.csv')
st.head()
st.write(dt.head(10))