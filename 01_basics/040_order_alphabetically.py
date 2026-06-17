# program to sort words in alphabetical order.

words = ["banana", "Apple", "cherry", "Date"]

# sorted() returns a completely new list
sorted_words = sorted(words, key=str.lower)

print("Original words:", words)
print("Sorted words:  ", sorted_words)