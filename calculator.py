class Vehicle():

    def drive(self):
        print("Vehicle is driving")
    
    def new_fn(self):
        print("my new fn")

class Car(Vehicle):
    pass
car=Car()
print(car.drive())

class BankAccount:
    def init(self,name):
        self._balance=0
        self.name=name
    def deposit(self,amount):
        self._balance+=amount
    def withdraw(self,amount):
        self._balance-=amount
    def get_balance(self):
        return self._balance
    def str(self):
        return f"Name:{self.name} and Balance:Hidden"
    
prakriti=BankAccount("prakriti")
prakriti.deposit(10000)
print(prakriti)
print(prakriti.get_balance)
prakriti.withdraw(100)
prakriti.deposit(500)
prakriti.withdraw(600)
print(prakriti.get_balance())