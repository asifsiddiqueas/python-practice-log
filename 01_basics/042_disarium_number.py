# python program to check if the given number is a Disarium number.
def is_disarium(n):
    # Convert number to string so we can loop through each digit
    num_str = str(n)
    
    total = 0
    
    # Loop through the string by index
    for i in range(len(num_str)):
        digit = int(num_str[i])
        position = i + 1
        
        # Add the digit raised to its position's power
        total += digit ** position
        
    # Check if our total matches the original number
    return total == n

# Test it out...
number = 135 

if is_disarium(number):
    print(f"{number} is a Disarium number!")
else:
    print(f"{number} is NOT a Disarium number.")