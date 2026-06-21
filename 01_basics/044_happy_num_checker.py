# python program to check if the given number is Happy Number.
def is_happy_number(n):
    """
    Checks if a given positive integer is a Happy Number.
    """
    # using a set to keep track of numbers we've already seen.
    # This is crucial to detect infinite loops...
    seen_numbers = set()
    
    # Continue looping as long as n is not 1 and we haven't entered a cycle
    while n != 1 and n not in seen_numbers:
        # Add the current number to our set of seen numbers
        seen_numbers.add(n)
        
        # Calculate the sum of the squares of the digits
        total = 0
        while n > 0:
            digit = n % 10       # Get the last digit
            total += digit ** 2  # Square it and add to total
            n //= 10             # Remove the last digit from n
            
        # Update n to the new total for the next iteration
        n = total
        
    # If the loop finished and n is 1, it's a happy number
    return n == 1

# Example Usage
test_number = 19

if is_happy_number(test_number):
    print(f"{test_number} is a Happy Number!")
else:
    print(f"{test_number} is not a Happy Number (it's a sad/unhappy number).")