# Python program to Count occurrences of an element in a list.
def count_item(items_list, target):
    # Simply call .count() on the list and pass in the item you are looking for
    return items_list.count(target)

# Example
my_items = [10, 20, 10, 30, 10, 40, 50]
item_to_find = 10

total_count = count_item(my_items, item_to_find)

print(f"The list: {my_items}")
print(f"The number {item_to_find} appears {total_count} times.")