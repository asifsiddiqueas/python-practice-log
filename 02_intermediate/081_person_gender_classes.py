"""
Defines a base Person class and two child classes (Male and Female) to demonstrate inheritance and method overriding.
Input: None (class instantiation)
Output: Prints the string "Male" or "Female" depending on which child class's getGender() method is called.
"""

class Person:
    """A base class establishing the interface for person types."""
    def getGender(self):
        # enforce implementation in subclasses
        raise NotImplementedError("Subclasses must implement getGender()")

class Male(Person):
    """Child class representing a male."""
    def getGender(self):
        print("Male")

class Female(Person):
    """Child class representing a female."""
    def getGender(self):
        print("Female")

# test cases
person_male = Male()
person_female = Female()

person_male.getGender()
# expected output: Male

person_female.getGender()
# expected output: Female