import pandas as pd
import yfinance as yf
import streamlit as st
from module import Fund, Account  # Assuming we saved our Fund and Account classes in 'fund_module.py'


import auth

conn = auth.Connect()
db = conn.get_collection('fund')

st.write(db.document("fund").get().to_dict()['value'])

docs = conn.get_collection('holdings').stream()
items = list(map(lambda x: {'ticker': x.id}, docs))
st.write(items)


fund_value = db.document("fund").get().to_dict()['value']
fund_shares = db.document("fund").get().to_dict()['shares']

st.metric('NAV', fund_value)
st.metric('Shares', fund_shares)
st.metric('Price', fund_value / fund_shares)

fund = Fund()
saleh = Account("saleh", fund)
ruyuf = Account("ruyuf", fund)

account = st.radio('account', ['saleh', 'ruyuf'])
amount = st.number_input('amount', min_value=0)
submitted = st.button("Submit")

if submitted:
    saleh.contribute(amount)



