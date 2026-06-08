arr = [12, 45, 7, 89, 34]

largest = arr[0]

for i in arr:
    if i > largest:
        largest = i

print("Largest element is:", largest)