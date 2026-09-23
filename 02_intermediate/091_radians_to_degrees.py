"""
Python program to create a function that takes an angle in radians and returns the corresponding angle
in degrees rounded to one decimal place..

Examples:
    radians_to_degrees(1) -> 57.3
    radians_to_degrees(20) -> 1145.9
    radians_to_degrees(50) -> 2864.8
"""

import math


def radians_to_degrees(rad: float | int) -> float:
    return round(math.degrees(rad), 1)


if __name__ == "__main__":
    # Output from the function
    for rad in (1, 20, 50):
        print(f"Degree of {rad} radian is {radians_to_degrees(rad)}")