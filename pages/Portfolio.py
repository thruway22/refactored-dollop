import streamlit as st
import pandas as pd

st.title('Portfolio Page')

df = pd.DataFrame()

st.data_editor(df)