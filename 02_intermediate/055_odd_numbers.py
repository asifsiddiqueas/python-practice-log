# Python program to print odd numbers in a List.
def get_odds(nums):
    return [n for n in nums if n % 2 != 0]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odds = get_odds(numbers)

print(f"Original numbers: {numbers}")
print(f"Odd numbers: {odds}")