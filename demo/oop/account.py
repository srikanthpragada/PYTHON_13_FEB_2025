class Account:
    def __init__(self, acno, ahname, balance = 0):
        self.acno = acno
        self.ahname = ahname
        self.balance = balance

    def depsoit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def getbalance(self):
        return self.balance

a1 = Account(1, "Larry", 10000)
a1.depsoit(5000)
print(a1.getbalance())
