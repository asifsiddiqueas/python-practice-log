# Write a Python program to swap two variables.

# user defined variables
a = input("Enter the value of a: ")
b = input("Enter the value of b: ")

#Display the actual value provided by the user
print(f"The actual value of a is: {a}")
print(f"The actual value of b is: {b}")

# swapping the variables using temp variable/container
temp = a
a = b
b = temp

#Display the final output
print(f"The swapped value of a is {a}")
print(f"The swapped value of b is {b}")