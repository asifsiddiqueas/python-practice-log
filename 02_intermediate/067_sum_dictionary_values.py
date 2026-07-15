# Python program to find the sum of all items in a dictionary.
def get_dict_sum_fast(data_dict):

    # .values() grabs just the numbers, and sum() adds them all up!
    return sum(data_dict.values())

# Example
expenses = {
    'groceries': 150,
    'utilities': 80,
    'internet': 50,
    'gas': 40
}

total = get_dict_sum_fast(expenses)

print(f"Our expenses: {expenses}")
print(f"Total spent: ${total}")
# Output: Total spent: $320