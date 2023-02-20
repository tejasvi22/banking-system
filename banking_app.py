class User():
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def shoe_details(self):
        print("Personal details")
        print("")
        print("Name ",self.name)
        print("Age ",self.age)
        print("Gender ",self.gender)

class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self,amount):
        self.balance += amount
        print("Account balance has been updated : $", self.balance)
    
    def withdrawl(self,amount):
        if self.balance > amount:
            self.balance -= amount
            print("Account balance has been updated : $", self.balance)
        else:
            print("Insufficient balance, account balance available : $", self.balance)
    
    def view_balance(self):
        self.shoe_details()
        print("Account balance available : $", self.balance)

rahul = Bank('rahul',21,'M')

rahul.deposit(100)
rahul.withdrawl(10)
rahul.deposit(500)
rahul.withdrawl(1000)
rahul.deposit(500)
rahul.view_balance()