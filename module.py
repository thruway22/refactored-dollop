# Adjustments to module.py

from datetime import datetime
import auth

conn = auth.Connect()

class Fund:
    def __init__(self):
        # Initial amount and shares
        self.timestamp = str(datetime.now().replace(microsecond=0))

    @property
    def latest_entry(self):
        entries = [x.id for x in conn.get_collection('fund').stream()]
        return str(max(datetime.strptime(ts, '%Y-%m-%d %H:%M:%S') for ts in entries))

    @property
    def fund_value(self):
        return conn.get_collection('fund').document(self.latest_entry).get().to_dict()['value']

    @property
    def fund_shares(self):
        return conn.get_collection('fund').document(self.latest_entry).get().to_dict()['shares']

    @property
    def share_price(self):
        return self.fund_value / self.fund_shares if self.fund_shares > 0 else 1.0

    def add_money(self, amount):
        # Calculate shares to be issued based on the current share price
        shares_issued = amount / self.share_price
        # Calculate new fund value and total shares
        new_value = self.fund_value + amount
        new_shares = self.fund_shares + shares_issued
        # Push the updated values to Firestore with the current timestamp as the document name
        conn.get_collection("fund").document(self.timestamp).set({'value': new_value, 'shares': new_shares})
        return shares_issued

# Adjustments to the Account class in module.py

class Account:
    def __init__(self, name, fund):
        self.name = name
        self.fund = fund

    @property
    def latest_entry(self):
        entries = [x.id for x in conn.get_collection(self.name).stream()]
        if entries:
            return str(max(datetime.strptime(ts, '%Y-%m-%d %H:%M:%S') for ts in entries))
        return None

    @property
    def cumulative_contribution(self):
        latest = self.latest_entry
        if latest:
            return conn.get_collection(self.name).document(latest).get().to_dict()['cumulative_contribution']
        return 0.0

    @property
    def cumulative_shares(self):
        latest = self.latest_entry
        if latest:
            return conn.get_collection(self.name).document(latest).get().to_dict()['cumulative_shares']
        return 0.0

    def contribute(self, amount):
        # Calculate shares received based on the fund's share price
        shares_received = amount / self.fund.share_price

        # Calculate cumulative values
        new_cumulative_contribution = self.cumulative_contribution + amount
        new_cumulative_shares = self.cumulative_shares + shares_received

        # Push the data to Firestore
        conn.get_collection(self.name).document(self.fund.timestamp).set({
            'transaction_contribution': amount,
            'transaction_shares': shares_received,
            'cumulative_contribution': new_cumulative_contribution,
            'cumulative_shares': new_cumulative_shares
        })

        # Update the fund's NAV and shares
        self.fund.add_money(amount)

        return shares_received

# This is the adjusted Account logic. Next, we'll integrate it with the app.py logic.


# This is just the adjusted module.py logic. I'll update app.py next.



# from datetime import datetime
# import auth

# conn = auth.Connect()

# class Fund:
#     def __init__(self):
#         # Initial amount and shares
#         self.timestamp = str(datetime.now().replace(microsecond=0))

#     @property
#     def latest_entry(self):
#         entries = [x.id for x in conn.get_collection('fund').stream()]
#         return str(max(datetime.strptime(ts, '%Y-%m-%d %H:%M:%S') for ts in entries))

#     @property
#     def fund_value(self):
#         return conn.get_collection('fund').document(self.latest_entry).get().to_dict()['value']

#     @property
#     def fund_shares(self):
#         return conn.get_collection('fund').document(self.latest_entry).get().to_dict()['shares']

#     @property
#     def share_price(self):
#         # Share price is total amount divided by total shares, if no shares exist yet, price is 1
#         return self.fund_value / self.fund_shares if self.fund_shares > 0 else 1.0

#     def update_nav(self, new_nav):
#         shares = self.fund_shares
#         conn.get_collection("fund").document(str(datetime.now().replace(microsecond=0))).set({'value': new_nav, 'shares': shares})

#     def add_money(self, amount):
#         # Calculate shares to be issued based on the current share price
#         shares_issued = amount / self.share_price
#         # Update total amount and total shares
#         conn.get_collection("fund").document("fund").update({"value": (self.fund_value + amount)})
#         conn.get_collection("fund").document("fund").update({"shares": (self.fund_shares + shares_issued)})
#         # self.fund_value += amount
#         # self.fund_shares += shares_issued
#         return shares_issued

# # fund = Fund()
# # fund.add_money(100)  # Initial funding
# # fund.fund_shares, fund.share_price  # Check initial shares and share price

# class Account:
#     def __init__(self, name, fund):
#         self.name = name
#         self.fund = fund
#         self.account_con = conn.get_collection('account').document(name).get().to_dict()['con']
#         self.account_shares = conn.get_collection('account').document(name).get().to_dict()['shares']

#     def contribute(self, amount):
#         # Use the fund's add_money method to get the shares for the contributed amount
#         shares_received = self.fund.add_money(amount)

#         # Update the account's total shares
#         # self.fund_shares += shares_received
#         return shares_received

# # # Testing the Account class
# # fund = Fund()
# # alice = Account("Alice", fund)
# # bob = Account("Bob", fund)

# # alice.contribute(50)
# # bob.contribute(100)

# # alice.fund_shares, bob.fund_shares, fund.share_price

