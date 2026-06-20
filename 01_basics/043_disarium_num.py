# python program to print all disarium numbers between 1 to 100...
def is_disarium(n):
    # Convert number to string to access each digit by index
    num_str = str(n)
    total = 0
    
    # Calculate the sum of digits powered to their positions
    for i in range(len(num_str)):
        digit = int(num_str[i])
        position = i + 1
        total += digit ** position
        
    return total == n

print("Disarium numbers between 1 and 100 are:")

# Loop through numbers 1 to 100 (101 is exclusive)
for num in range(1, 101):
    if is_disarium(num):
        # Print on the same line separated by a space
        print(num, end=" ")