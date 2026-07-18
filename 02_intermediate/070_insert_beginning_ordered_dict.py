# Python program to insertion at the beginning in OrderedDict.
from collections import OrderedDict

def insert_at_beginning_ordered(odict, key, value):
    # inserts at the end by default
    odict[key] = value
    
    # shift it to the front
    odict.move_to_end(key, last=False)
    
    return odict

# test setup
my_ordered_dict = OrderedDict([('apple', 10), ('banana', 20)])
print(f"Original dictionary: {my_ordered_dict}")

# push mango to the front
updated_dict = insert_at_beginning_ordered(my_ordered_dict, 'mango', 30)

print(f"Processed dictionary: {updated_dict}")
# mango should be the first item now