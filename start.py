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
