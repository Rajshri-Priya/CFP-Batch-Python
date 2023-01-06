class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number   # private variable
        self.__balance = balance        # private variable
    
    def get_balance(self):
        return self.__balance       # private variable
    
    def deposit(self, amount):
        self.__balance += amount          # private variable
    
    def withdraw(self, amount):
        if self.__balance - amount >= 0:
            self.__balance -= amount
            return True
        else:
            return False

# create a new BankAccount object
my_account = BankAccount(123456789, 1000)

# deposit 500
my_account.deposit(500)

# withdraw 200
success = my_account.withdraw(200)
if success:
    print("Withdrawal successful")
else:
    print("Insufficient funds")

# try to withdraw more than the balance
success = my_account.withdraw(5000)
if success:
    print("Withdrawal successful")
else:
    print("Insufficient funds")

# print the current balance
print("Current balance:", my_account.get_balance())
