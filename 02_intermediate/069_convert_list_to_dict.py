# Python program to convert key-values list to flat dictionary.
def convert_pairs_to_dict(paired_list):

    # dict() handles iterables of pairs natively, no need to write a loop
    return dict(paired_list)

# dummy data to test it out
my_list_of_pairs = [
    ("apple", 100), 
    ("banana", 200), 
    ("cherry", 300)
]

flat_dict = convert_pairs_to_dict(my_list_of_pairs)

print(f"List of pairs: {my_list_of_pairs}")
print(f"Flat dictionary: {flat_dict}")
# should print: {'apple': 100, 'banana': 200, 'cherry': 300}