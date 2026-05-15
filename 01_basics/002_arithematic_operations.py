# Write a Python program to do arithmetical operations addition and division.

#Addition task
num1 = float(input("Enter your first number\n"))
num2 = float(input("Enter your Second number\n"))
sum = num1 + num2
print(f"sum of your two number is : {sum}")

#Division Task

num3 = float(input("Enter your dividend\n"))
num4 = float(input("Enter your Divisor\n"))

#Checking for division by zero to prevent crashing of this program
if num4 == 0:
    print("Invalid, Division by zero is not allowed...consider the output as infinite")

else:
    Division = num3 / num4
    print(f"The division of your given data is : {Division}\n")

    #End of the program