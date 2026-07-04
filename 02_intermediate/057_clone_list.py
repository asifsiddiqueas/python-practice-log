# Python program to Cloning or Copying a list.
def clone_list(items):
    return items.copy()

# Our starting list
my_list = [1, 2, 3, 4, 5]

# Clone it
cloned_list = clone_list(my_list)

print(f"The original list is: {my_list}")
print(f"The cloned list is:   {cloned_list}")