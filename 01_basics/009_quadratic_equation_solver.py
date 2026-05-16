# Program to solve the quadratic equation.
# Sample of Quadratic Equation is: ax**2 + bx + c = 0
# Roots value farmula: -b +- (math.sqrt(b**2 - 4 ac))/2a  [just for understanding purpose]
# Discriminant value to break the code = (b**2 - 4ac)

import math

#user defined input
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

#Defining Discriminant value to break the code pattern
discriminant = (b**2 - 4*a*c)

# Loop statements for multiple possibilities
if a==0:
    print("This is not a Quadratic Equation, It's Linear Equation")
elif discriminant > 0:
    root1 = (-b + math.sqrt(discriminant))/(2*a)
    root2 = (-b - math.sqrt(discriminant))/(2*a)
    print(f"The value of root 1 is: {root1}")
    print(f"The value of root 2 is: {root2}")
elif discriminant ==0:
    real_root = -b/(2*a)
    print(f"The unique real root is: {real_root}")
else:
    real_root = -b/(2*a)
    imaginary_root = math.sqrt(abs(discriminant))/(2*a)
    print(f"the value of root 1 is: {real_root} + {imaginary_root}i")
    print(f"the value of root 2 is: {real_root} - {imaginary_root}i")