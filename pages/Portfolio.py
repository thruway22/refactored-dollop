import streamlit as st
import pandas as pd

st.title('Portfolio Page')

df = pd.DataFrame(columns=['ticker', 'target'])

st.data_editor(df, num_rows='dynamic')