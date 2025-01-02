# class Vehicle():

#     def drive(self):
#         print("Vehicle is driving")
    
#     def new_fn(self):
#         print("my new fn")

# class Car(Vehicle):
#     pass
# car=Car()
# print(car.drive())

# class BankAccount:
#     def init(self,name):
#         self._balance=0
#         self.name=name
#     def deposit(self,amount):
#         self._balance+=amount
#     def withdraw(self,amount):
#         self._balance-=amount
#     def get_balance(self):
#         return self._balance
#     def str(self):
#         return f"Name:{self.name} and Balance:Hidden"
    
# prakriti=BankAccount("prakriti")
# prakriti.deposit(10000)
# print(prakriti)
# print(prakriti.get_balance)
# prakriti.withdraw(100)
# prakriti.deposit(500)
# prakriti.withdraw(600)
# print(prakriti.get_balance())

#list
# info={
#     "prakriti":"khatri",
#     "college":"texas",
#     "mothere":"nabina",
#     "age":21,

# }
# print(info)

# class Vector:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def __add__(self,other):
#         return Vector(self.x+other.x,self.y+other.y)
#     def __sub__(self,other):
#         return Vector(self.x-other.x,self.y-other.y)
#     def __mul__(self,scalar):
#         return Vector(self.x*scalar.x,self.y*scalar.y)
#     def __str__(self):
#         return f"vector:{self.x,{self.y}}"
    
# v1=Vector(1,2)
# v2=Vector(3,4)
# v3=Vector(3,4)
# v4=Vector(3,4)
# result_vector=v1+v2
# print(result_vector)
 
 #operator 
class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,*others):
        sum_vector=Vector(self.x,self.y)
        for other in others:
            sum_vector=Vector(sum_vector.x + other.x, sum_vector.y+other.y)
            return sum_vector
    def __sub__(self,*others):
        sub_vector=Vector(self.x,self.y)
        for other in others:
            sub_vector=Vector(sub_vector.x- other.x,sub_vector.y-other.y)
            return sub_vector
    def __mul__(self,*others):
        mul_vectors=Vector(self.x,self.y)
        for other in others:
            mul_vectors=Vector(mul_vectors.x*other,mul_vectors.y*other)
        return mul_vectors
    def __str__(self):
        return f"vector:({self.x},{self.y})"

v1=Vector(1,2)
v2=Vector(3,4)
v3=Vector(3,4)
v4=Vector(3,4)
result_vector=v1+v2+v3+v4
print(result_vector)

try:
      result=10/0
except ZeroDivisionError as e:
    print("expection",e)
try:
    my_list=[1,2,3]
    print(my_list[5])
except IndexError as e:
    print("Exception",e)
class NoMoneyException(Exception):
    pass
class OutOfBudget(Exception):
    pass
balance
