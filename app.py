import pandas as pd
import yfinance as yf
import streamlit as st
from module import Fund, Account  # Assuming we saved our Fund and Account classes in 'fund_module.py'


import auth

conn = auth.Connect()
db = conn.get_collection('fund')

st.write(db.document("fund").get().to_dict()['value'])
