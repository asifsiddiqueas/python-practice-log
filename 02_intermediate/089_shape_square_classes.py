"""
Python program to Defines a base Shape class and a Square subclass to calculate and print geometric areas.
Input: A numeric length argument passed to the Square classes upon initialization.
Output: Prints the calculated area (length squared for Square, default 0 for generic Shape).
"""
class Shape:
    """Base class representing a general geometric shape."""
    def area(self):
        # default area is 0 for generic shapes
        print(0)


class Square(Shape):
    """Represent a square, inheriting from Shape."""
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        # override base method to calculate actual area
        print(self.length ** 2)


# testing
if __name__ == "__main__":
    generic_shape = Shape()
    print("Shape area default:")
    generic_shape.area()
    # expected output: 0

    square = Square(5)
    print("Square area (length = 5):")
    square.area()
    # expected output: 25