# Python program to Remove empty List from List.
def remove_empty(items):
    return [x for x in items if x != []]

# Our starting list with some empty lists mixed in
my_list = [1, 2, [], 3, [], [], 4, 5, []]

# Clean it up
cleaned_list = remove_empty(my_list)

print(f"Original list: {my_list}")
print(f"Cleaned list:  {cleaned_list}")