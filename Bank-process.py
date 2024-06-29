class Account:
    def __init__(self, account_id, name, initial_balance=0):
        self.account_id = account_id
        self.name = name
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_id, name, initial_balance=0):
        if account_id in self.accounts:
            return False  # Account ID already exists
        self.accounts[account_id] = Account(account_id, name, initial_balance)
        return True

    def delete_account(self, account_id):
        if account_id in self.accounts:
            del self.accounts[account_id]
            return True
        return False

    def deposit_money(self, account_id, amount):
        if account_id in self.accounts and amount > 0:
            return self.accounts[account_id].deposit(amount)
        return False

    def withdraw_money(self, account_id, amount):
        if account_id in self.accounts:
            return self.accounts[account_id].withdraw(amount)
        return False

    def transfer_money(self, from_account_id, to_account_id, amount):
        if (from_account_id in self.accounts and to_account_id in self.accounts and
                self.accounts[from_account_id].balance >= amount and amount > 0):
            self.accounts[from_account_id].withdraw(amount)
            self.accounts[to_account_id].deposit(amount)
            return True
        return False

    def get_account_balance(self, account_id):
        if account_id in self.accounts:
            return self.accounts[account_id].balance
        return None

# Example usage
bank = Bank()

# Creating accounts
bank.create_account("123", "Alice", 1000)
bank.create_account("456", "Bob", 500)

# Deposit money
bank.deposit_money("123", 200)

# Withdraw money
bank.withdraw_money("456", 100)

# Transfer money
bank.transfer_money("123", "456", 300)

# Get account balances
print("Alice's balance:", bank.get_account_balance("123"))
print("Bob's balance:", bank.get_account_balance("456"))

# Delete an account
bank.delete_account("123")
