"""
Write a Python program where it is given that, the side length x, find the area of a regular hexagon rounded to 1 decimal place.

Examples:
    area_of_hexagon(1) -> 2.6
    area_of_hexagon(2) -> 10.4
    area_of_hexagon(3) -> 23.4
"""

import math


def area_of_hexagon(x: float | int) -> float:
    area = (3 * math.sqrt(3) * (x ** 2)) / 2
    return round(area, 1)


if __name__ == "__main__":
    # Output from the function
    for side in (1, 2, 3):
        print(f"Area of hexagon with side {side} is {area_of_hexagon(side)}")