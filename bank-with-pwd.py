class Account:
    def __init__(self, account_id, name, password, initial_balance=0):
        self.account_id = account_id
        self.name = name
        self.password = password
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

    def create_account(self, account_id, name, password, initial_balance=0):
        if account_id in self.accounts:
            return False  # Account ID already exists
        self.accounts[account_id] = Account(account_id, name, password, initial_balance)
        return True

    def delete_account(self, account_id, password):
        if account_id in self.accounts and self.accounts[account_id].password == password:
            del self.accounts[account_id]
            return True
        return False

    def deposit_money(self, account_id, amount, password):
        if account_id in self.accounts and self.accounts[account_id].password == password:
            return self.accounts[account_id].deposit(amount)
        return False

    def withdraw_money(self, account_id, amount, password):
        if account_id in self.accounts and self.accounts[account_id].password == password:
            return self.accounts[account_id].withdraw(amount)
        return False

    def transfer_money(self, from_account_id, to_account_id, amount, password):
        if (from_account_id in self.accounts and to_account_id in self.accounts and
                self.accounts[from_account_id].password == password and
                self.accounts[from_account_id].balance >= amount and amount > 0):
            self.accounts[from_account_id].withdraw(amount)
            self.accounts[to_account_id].deposit(amount)
            return True
        return False

    def get_account_balance(self, account_id, password):
        if account_id in self.accounts and self.accounts[account_id].password == password:
            return self.accounts[account_id].balance
        return None

# Example usage
bank = Bank()

# Creating accounts
bank.create_account("123", "Alice", "alice_pass", 1000)
bank.create_account("456", "Bob", "bob_pass", 500)

# Deposit money
bank.deposit_money("123", 200, "alice_pass")

# Withdraw money
bank.withdraw_money("456", 100, "bob_pass")

# Transfer money
bank.transfer_money("123", "456", 300, "alice_pass")

# Get account balances
print("Alice's balance:", bank.get_account_balance("123", "alice_pass"))
print("Bob's balance:", bank.get_account_balance("456", "bob_pass"))

# Delete an account
bank.delete_account("123", "alice_pass")

'''
Assumptions:

    Account IDs are unique and represented as strings.
    Passwords are required for account creation and are used for verification during account operations.
    Initial balance is optional when creating an account; if not provided, it defaults to 0.
    Deposits and withdrawals must be positive amounts.
    Transfers only happen if the sender has enough balance, the amount is positive, and the password is correct.
    The system doesn't handle errors or edge cases like non-numeric inputs, negative values, or incorrect account IDs.

'''
