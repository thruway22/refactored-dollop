import streamlit as st

st.title('Transactions Page')

tickers = st.multiselect('Choose ticker', ['VTI', 'AVUV', 'VXUS'])

st.write(tickers)

for i in tickers:
    st.write(i, 'shares', 'cost', 'fee') 