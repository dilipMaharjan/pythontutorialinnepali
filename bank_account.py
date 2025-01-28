class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number  # Public attribute
        self.__balance = balance             # Private attribute

    # Public method to get balance
    def get_balance(self):
        return self.__balance

    # Public method to deposit
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    # Public method to withdraw
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance or invalid amount")

# Usage
account = BankAccount("123456", 1000)
print(account.get_balance())  # Output: 1000
account.deposit(500)
print(account.get_balance())
account.withdraw(300)
print(account.get_balance())  # Output: 1200