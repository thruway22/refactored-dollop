import pandas as pd
import yfinance as yf
import streamlit as st
from datetime import datetime
from module import Fund, Account  # Assuming we saved our Fund and Account classes in 'fund_module.py'


import auth

conn = auth.Connect()

value = st.number_input('value', min_value=0)
shares = st.number_input('shares', min_value=0)
submitted = st.button("Submit")
if submitted:
    conn.get_collection("fund").document(
        str(datetime.now().replace(microsecond=0))
        ).set({'value': value, 'shares': shares})
    

fund = Fund()

st.metric('NAV', fund.fund_value)
st.metric('Shares', fund.fund_shares)
st.metric('Price', fund.share_price)

# fund = Fund()
# saleh = Account("saleh", fund)
# ruyuf = Account("ruyuf", fund)

# account = st.radio('account', ['saleh', 'ruyuf'])
# amount = st.number_input('amount', min_value=0)
# submitted = st.button("Submit")

# if submitted:
#     saleh.contribute(amount)



