import streamlit as st
from module import Fund, Account

# Create a fund instance and accounts for each person
fund = Fund()

# Streamlit Interface
st.title("Fund Tracker")

# 1. Input current NAV
current_nav = st.number_input("Enter the current NAV:", value=fund.fund_value)

# 2. Select account and input their contribution
account_name = st.selectbox("Select Account:", ['saleh', 'ruyuf'])  # Add more names if needed
account = Account(account_name, fund)
contribution = st.number_input(f"Enter {account_name}'s contribution:")

# 3. Calculate and display shares for the account based on the current share price
shares_received = contribution / fund.share_price
st.write(f"{account_name} will receive {shares_received} shares for a contribution of {contribution}.")

# 4. Button to push the updated NAV and shares to Firestore
if st.button("Update Fund", type='primary', use_container_width=True):
    account.contribute(contribution)
    st.success(f"Updated fund and {account_name}'s account successfully!")
    st.experimental_rerun()

st.divider()

# Display fund metrics
col1, col2, col3 = st.columns(3)
col1.metric('NAV', fund.fund_value)
col2.metric('Shares', fund.fund_shares)
col3.metric('Price', fund.share_price)
