x = float(input("Enter a number: "))
result = (((2 * x) + 10) / 2) - x

print("The result is:", result)

input("enter the number")




length = float(input("enter the length of the rectangle"))
width=float(input("enter the width of the rectangle"))
area=length*width
perimeter=2 *(length+width)
print(f"rectangle area{area:2f}")
print(f"rectangle perimater{perimeter:2f}")


radius= float(input("enter the radius of the circle "))
area = 22/7* radius**2
circumference = 2 * 22/7 * radius
print(f"circle area{area}")
print(f"circle circumference{circumference}")


#Currency (using hardcoded exchange rates)
exchange_rates = {
    "USD_TO_INR": 82.5,
    "USD_TO_EUR": 0.91,
    "INR_TO_USD": 0.012,
    "INR_TO_EUR": 0.011,
}

amount = float(input("Enter the amount: "))
conversion_type = input("Enter the conversion (e.g., USD_TO_INR, INR_TO_USD): ").upper()
if conversion_type in exchange_rates:
    converted_amount = amount * exchange_rates[conversion_type]
    print(f"{amount} {conversion_type.split('TO')[0]} is equal to {converted_amount:.2f} {conversion_type.split('TO')[1]}")
else:
    print("Invalid conversion type. Please try again.")


        
#to calculate simple interest 
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual rate of interest (in %): "))
time = float(input("Enter the time (in years): "))
simple_interest = (principal*rate*time)/100
print(f"The Simple Interest is: {simple_interest:.2f}")


#Calculate the area and perimeter of shapes (triangle))
a = float(input("Enter the lenght of one side:"))
b = float(input("Enter the base of  triangle:"))
c = float(input("Enter the heigth of triangle:"))
Area=1/2*b*c
Perimeter=a+b+c
print(f"The Area is:{Area:.2f}")
print(f"The Perimeter is: {Perimeter:.2f}" )


#check wheather the number is a multiple of another number.
num1=float(input("enter a first number"))
num2=float(input("enter a second number"))

