"""
A class-based generator that yields numbers divisible by 7 within a range from 0 to n.
Input: An integer n representing the upper limit of the range (e.g., 50)
Output: A generator yielding integers divisible by 7 (e.g., 0, 7, 14, 21, 28, 35, 42, 49)
"""

class DivisibleBySeven:
    
    def __init__(self, n):
        self.n = n

    def generate(self):
        # step through the range by 7 and yield values directly
        yield from range(0, self.n + 1, 7)

# test cases
n_value = 50
divisible_gen = DivisibleBySeven(n_value)

# evaluate the generator into a list for output
processed_data = list(divisible_gen.generate())

print(f"Target range: 0 to {n_value}")
print(f"Divisible by 7: {processed_data}")
# expected output: [0, 7, 14, 21, 28, 35, 42, 49]