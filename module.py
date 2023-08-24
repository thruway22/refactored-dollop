import auth

class Fund:
    def __init__(self):
        # Initial amount and shares
        self.total_amount = 0.0
        self.total_shares = 0.0

    @property
    def share_price(self):
        # Share price is total amount divided by total shares, if no shares exist yet, price is 1
        return self.total_amount / self.total_shares if self.total_shares > 0 else 1.0

    def add_money(self, amount):
        # Calculate shares to be issued based on the current share price
        shares_issued = amount / self.share_price
        # Update total amount and total shares
        self.total_amount += amount
        self.total_shares += shares_issued
        return shares_issued

# fund = Fund()
# fund.add_money(100)  # Initial funding
# fund.total_shares, fund.share_price  # Check initial shares and share price

class Account:
    def __init__(self, name, fund):
        self.name = name
        self.fund = fund
        self.total_shares = 0.0

    def contribute(self, amount):
        # Use the fund's add_money method to get the shares for the contributed amount
        shares_received = self.fund.add_money(amount)
        # Update the account's total shares
        self.total_shares += shares_received
        return shares_received

# # Testing the Account class
# fund = Fund()
# alice = Account("Alice", fund)
# bob = Account("Bob", fund)

# alice.contribute(50)
# bob.contribute(100)

# alice.total_shares, bob.total_shares, fund.share_price

