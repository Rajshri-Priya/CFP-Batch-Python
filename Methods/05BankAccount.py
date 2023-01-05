# using instance variable ,instance method ,class variable,class method and static method

class BankAccount:
  # Class variable
  interest_rate = 0.03
  fees = 5.0

  def __init__(self, balance):
    self.balance = balance

  # Instance method
  def apply_interest(self):
    self.balance += self.balance * self.interest_rate

  # Class method
  @classmethod
  def change_interest_rate(cls, new_rate):
    cls.interest_rate = new_rate

  # Static method
  @staticmethod
  def is_valid_amount(amount):
    return amount >= 0

account1 = BankAccount(100)
account2 = BankAccount(200)

account1.apply_interest()
print(account1.balance)  # Output: 103.0
print(account2.balance)  # Output: 200.0

BankAccount.change_interest_rate(0.05)
account2.apply_interest()
print(account1.balance)  # Output: 103.0
print(account2.balance)  # Output: 210.0

print(BankAccount.is_valid_amount(50))  # Output: True
print(BankAccount.is_valid_amount(-50))  # Output: False
