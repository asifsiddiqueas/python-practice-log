# python program to remove punctuation from a string
import string

text = "Hello world! How is it going? This is a test... right?"

# str.maketrans creates a mapping table.
#  
# We tell it to map nothing to nothing, and remove all string.punctuation
translator = str.maketrans('', '', string.punctuation)

clean_text = text.translate(translator)

print(clean_text)