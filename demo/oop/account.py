class InsufficientBalanceError(Exception):
    def __init__(self, balance, amount):
        self.message = f'Insufficient balance {balance} for withdraw of {amount}'
    def __str__(self):
        return self.message

class Account:
    min_balance = 10000

    @staticmethod
    def get_min_balance():
        return Account.min_balance

    def __init__(self, acno, ahname, balance=0):
        self.acno = acno
        self.ahname = ahname
        self.balance = balance

    def depsoit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= Account.min_balance:
            self.balance -= amount
        else:
            raise InsufficientBalanceError(self.balance, amount)

    def getbalance(self):
        return self.balance


a1 = Account(1, "Larry", 10000)
a1.depsoit(5000)
try:
    a1.withdraw(50000)
    print(a1.getbalance())
except Exception as ex:
    print(ex)

print("The End")
