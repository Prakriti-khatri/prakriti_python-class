while True:
    user_number =int(input("enter your number"))
    result_number=user_number* 2
    print(f"double number={result_number}")
    result_number = result_number +10
    print(f"add 10={result_number}")
    print(f"divide 2={result_number}")
    result_number = result_number/2
    result_number=result_number-user_number
    print(f"final result={result_number}")
    user_choice=

user_choice=input("""
 1.km to miles
2. miles to km
3.centermeter to inch   
4.inch to centimeter
"""  )
if user_choice=="1":
    user_input=float(input("enter km"))
    result =user_input *0.621371
    print(f"{user_input} km ={result}=miles")

elif user_choice=="2":
   user_input=float(input("enter miles"))
   result=user_input*1.60934
   print(f"{user-input} miles={result}=miles")

elif user_choice=="3":
    user_input=float(input("enter centimeter"))
    result=user_input*0.393701
    print(f"{user_input} centimeter={result}=centimeter")

elif user_choice=="3":
    user_input=float(input("enter inch"))
    result=user_input*2.45
    print(f"{user_input}inch={result}=inch")

    user_choice=input("""
     1.circle
    2.rectangle
    3. trangle""" )

    if user_choice=="1":
        user_radius=float(input("enter radius"))
        result_area=3.14* user_radius**2
        print(f"area={result_area}")
        result=perimeter=2*3.14* user_radius

        #while
        import random_
        random_number = random.randin(1,100)
        while true:
            user_guess  

            empty_list=[]  
            empty_list.append("apple")
            empty_list.append("banana")
            print(empty_list)


            empty_list=[]  
empty_list.append("apple")
empty_list.append("banana")
empty_list.append("kiwi")
empty_list.append("papaya")
for index, fruit in enumerate(empty_list):
    print(f"item position:{index}and value:{fruit}")

fruits=("apple","banana","cherry","straberry","raspberry")
print(fruits[1])
(green ,yellow ,*red)=fruits
print(green,yellow,red)

fruits={"apple","banana","cherry","straberry"}
for item in fruits:
    print(item)
    fruits.add("apple")
    print(fruits)
fruits.remove("banana")
print(fruits)
