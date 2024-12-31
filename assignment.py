#palindrome
def is_palindrome(p):
    return p == p [::-1]
print(is_palindrome("abc"))#true
print(is_palindrome("aabbaa"))#true
print(is_palindrome("abbbb"))#false
print(is_palindrome("baabbb"))#false


#area of circle
def calculate_area_of_circle(a):
    return 3.14 *radius *radius
radius = float(input("enter the radius of area"))
area= calculate_area_of_circle(radius)
print(f"the area of the circle with radius{radius}is:{area}")
