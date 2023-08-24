import pandas as pd
import yfinance as yf
import streamlit as st
from module import Fund, Account  # Assuming we saved our Fund and Account classes in 'fund_module.py'


import auth

conn = auth.Connect()
db = conn.get_collection('fund')

db.document("fund").get()




# Create a fund instance and accounts for each person
fund = Fund()
alice = Account("Alice", fund)
bob = Account("Bob", fund)
charlie = Account("Charlie", fund)

def display_fund_info():
    st.write("### Fund Info")
    st.write(f"Total Amount: ${fund.total_amount}")
    st.write(f"Total Shares: {fund.total_shares}")
    st.write(f"Share Price: ${fund.share_price}")

def display_contribution_section(account):
    st.write(f"### {account.name}'s Contribution")
    contribution = st.number_input(f"{account.name}, enter your monthly contribution:", value=0.0)
    if st.button(f"Contribute for {account.name}"):
        account.contribute(contribution)
        st.write(f"{account.name} received {contribution/fund.share_price} shares.")
        display_fund_info()

def main():
    st.title("Fund Tracker")
    display_fund_info()

    # Display contribution sections for each person
    display_contribution_section(alice)
    display_contribution_section(bob)
    display_contribution_section(charlie)

    # Display summary
    st.write("### Shares Owned")
    st.write(f"{alice.name}: {alice.total_shares} shares")
    st.write(f"{bob.name}: {bob.total_shares} shares")
    st.write(f"{charlie.name}: {charlie.total_shares} shares")

if __name__ == '__main__':
    main()
