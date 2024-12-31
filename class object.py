

# #todo list using python class and object
# # class Person:
# #     def __init__(self,name,age):
# #         self.name=name
# #         self.age=age
# #         #def __init__(self):
# #         #pass
# #         #pass
# # prakriti =Person("prakriti",20)
# # print(prakriti.name)
# # print(prakriti.age)

# # class PhoneFactory:
# #     model:None
# #     color:None
# #     is_android:None

# #     def __init__ (self,model,color,is_android):
# #       self.model=model
# #       self.color=color
# #       self.is_android=is_android
# #       print("phone created")

# #     def __str__(self):
# #             return f"{self.model}-{self.color}"
# #     def check_os(self):
# #             if self.is_android:
# #                 print("android")
# #             else:
# #                 print("ios")
# # oopo_phone_1 =PhoneFactory("a53","black","true")
# # print(oopo_phone_1)


# INVENTORY_FILE = "inventory.txt"
# LEADERBOARD_FILE = "leaderboard.txt"

# def save_to_file(filename, data, mode ="a"):
#     """Save data to file."""
#     with open (filename, mode) as file:
#         file.write(data + "\n")

# class TodoList:
#     def __init__(self):
#           self.tasks=[]
#     def add_task(self,task):
#           self.tasks.append(task)
#           print(f"task '{task}'added to the list.")

#     def remove_task(self, task):
#         if task in self.tasks:
#             self.tasks.remove(task)
#             print(f"task '{task}'removed from the task")
#         else:
#             print(f"task'{task}' not found in the list")
#     def update_task(self,old_task,new_task):
#         if old_task in self.tasks:
#             index=self.tasks.index(old_task)
#             self.tasks[index]= new_task
#             print(f"task updated to'{new_task}'")
#         else:
#             print(f"task'{old_task}'not found in the list")
#     def show_tasks(self):
#             if self.tasks:
#                 print("your todo list")
#                 for index,task in enumerate(self.tasks):
#                     print(f"'{index+1},{task}*")
#                 else:
#                     print("your todo list is empty")
# todo_list =TodoList()
# todo_list.add_task("Buy groceries")
# todo_list.add_task("finish the report")
# todo_list.add_task("call mom")
            
# todo_list.show_tasks()
# todo_list.remove_task("finish the task")
# todo_list.update_task("uy groceries","go for a walk")
# todo_list.show_tasks()


# example:1
# class MyIterator:
#     def __init__(self,data):
#         self.data=data
#         self.index=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.index >= len(self.data):
#             raise StopIteration
#         print(f"getting index:{self.index}")
#         value=self.data[self.index]
#         self.index+=1
#         return value
    
#     #using iteration
# my_list=[1,2,3,4,5]
# my_iter=MyIterator(my_list)
# for num in my_iter:
#     print(num)

# from abc import ABC, abstractmethod  
# class Vehicle():
#     #@abstractmethod
#     def drive(self):
#         print("Vehicle is driving")
#         #pass
#     def new_fn(self):
#             print("my new fn")
# class Car(Vehicle):
#          pass

# car=Car()
# print(car.drive())

#encapsulation
class BankAccount:
    def __init__(self,name):
        self._balance=0
        self.name=name
    def deposit(self,amount):
        self ._balance+=amount
    def withdraw(self,amount):
        self._balance-=amount
    def get_balance(self):
        return self._balance
    def __str__(self):
        return f"name:{self.name}and Balance:Hidden"
    
prakriti=BankAccount("Prakriti")
prakriti.deposit(100)
print(prakriti)
print(prakriti.get_balance())
prakriti.withdraw(50)
prakriti.deposit(400)
prakriti.withdraw(100)
print(prakriti.get_balance())