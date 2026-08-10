"""
Python Program to generate even numbers between 0 and n (inclusive) using an optimized range step.
Input: An integer n representing the upper limit of the sequence.
Output: Yields string representations of the even numbers.
"""

def generate_even_numbers(n):

    # step by 2 to generate evens directly without modulo checks
    for i in range(0, n + 1, 2):
        yield str(i)

# test cases
if __name__ == "__main__":
    try:
        user_input = int(input("Enter an integer n: "))
        
        # consume the generator and format as a comma-separated string
        result = ",".join(generate_even_numbers(user_input))
        
        print(result)
        # expected output for n=10: 0,2,4,6,8,10
    except ValueError:
        print("Invalid input. Please enter an integer.")