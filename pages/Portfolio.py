import streamlit as st
import pandas as pandas

st.title('Portfolio Page')

df = pd.DataFrame()

st.data_editor(df)