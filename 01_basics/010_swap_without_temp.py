# Program to swap two variables without temp variable.

a = (input("Enter the value of a: "))
b = (input("Enter the value of b: "))

print(f"The actual value of a is {a}")
print(f"The actual value of b is {b}")
# swapping without temp variable
a,b=b,a

# swapped values of a and b are
print(f"The swapped value of a is {a}")
print(f"The swapped value of b is {b}")