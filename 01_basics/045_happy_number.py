# Python program to print all happy numbers between 1 and 100.
def is_happy_number(n):
    seen_numbers = set()
    
    # Loop until we reach 1 (happy) or fall into a cycle (unhappy)
    while n != 1 and n not in seen_numbers:
        seen_numbers.add(n)
        
        # Calculate the sum of the squares of the digits
        total = 0
        while n > 0:
            digit = n % 10
            total += digit ** 2
            n //= 10
            
        n = total
        
    return n == 1

print("Happy numbers between 1 and 100 are:")

# Loop through numbers 1 to 100 (101 is exclusive)
for num in range(1, 101):
    if is_happy_number(num):
        # Print on the same line, separated by a comma and space
        print(num, end=", ")
        
# A neat trick to clear the trailing comma and move to a new line at the end
print("\b\b ")