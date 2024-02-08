class Account:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(self.balance)
    
    def withdraw(self, amount):
        if(self.balance < amount):
            return 0
        else:
            self.balance -= amount
            print (self.balance)
account = Account("name")

account.deposit(1000)
account.withdraw(500)
account.deposit(300)
account.withdraw(200)