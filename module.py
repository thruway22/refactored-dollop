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
    def fund_value(self)
        return self.fund_value = conn.get_collection('fund').document(
            self.latest_entry).get().to_dict()['value']

    @property
    def fund_shares(self)
        return self.fund_shares = conn.get_collection('fund').document(
            self.latest_entry).get().to_dict()['shares']

    @property
    def share_price(self):
        # Share price is total amount divided by total shares, if no shares exist yet, price is 1
        return self.fund_value / self.fund_shares if self.fund_shares > 0 else 1.0

    def update_nav(self, new_nav):
        shares = self.fund_shares
        conn.get_collection("fund").document(str(datetime.now().replace(microsecond=0))).set({'value': new_nav, 'shares': shares})

    def add_money(self, amount):
        # Calculate shares to be issued based on the current share price
        shares_issued = amount / self.share_price
        # Update total amount and total shares
        conn.get_collection("fund").document("fund").update({"value": (self.fund_value + amount)})
        conn.get_collection("fund").document("fund").update({"shares": (self.fund_shares + shares_issued)})
        # self.fund_value += amount
        # self.fund_shares += shares_issued
        return shares_issued

# fund = Fund()
# fund.add_money(100)  # Initial funding
# fund.fund_shares, fund.share_price  # Check initial shares and share price

class Account:
    def __init__(self, name, fund):
        self.name = name
        self.fund = fund
        self.account_con = conn.get_collection('account').document(name).get().to_dict()['con']
        self.account_shares = conn.get_collection('account').document(name).get().to_dict()['shares']

    def contribute(self, amount):
        # Use the fund's add_money method to get the shares for the contributed amount
        shares_received = self.fund.add_money(amount)

        # Update the account's total shares
        # self.fund_shares += shares_received
        return shares_received

# # Testing the Account class
# fund = Fund()
# alice = Account("Alice", fund)
# bob = Account("Bob", fund)

# alice.contribute(50)
# bob.contribute(100)

# alice.fund_shares, bob.fund_shares, fund.share_price

