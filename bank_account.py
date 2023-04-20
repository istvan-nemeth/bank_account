class Bank_account:
    def __init__(self, owner, balance, transactions):
        self.owner = owner
        self.balance = balance
        self.transactions = transactions

    def account_data(self):
        print(f"The owner's: {self.owner} balance: ${self.balance}")