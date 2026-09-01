"""
Python program using generator, to generate numbers between 0 and n (inclusive) that are divisible by both 5 and 7.
Input: An integer n representing the upper limit of the search range.
Output: Yields string representations of the numbers satisfying the divisibility condition...
"""

def generate_divisible_by_5_and_7(n):
    
    for i in range(n + 1):
        if i % 5 == 0 and i % 7 == 0:
            yield str(i)

# test cases
if __name__ == "__main__":
    try:
        user_input = int(input("Enter an integer n: "))
        
        # consume the generator and format as a comma-separated string
        result = ",".join(generate_divisible_by_5_and_7(user_input))
        
        print(result)
        # expected output for n=100: 0,35,70
    except ValueError:
        print("Invalid input. Please enter an integer.")