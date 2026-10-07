"""
Python program for the "Reverser" that takes a string as input and returns that string in reverse order, 
with the opposite case.

Examples:
    reverse("Hello World") -> "DLROw OLLEh"
    reverse("ReVeRsE") -> "eSrEvEr"
    reverse("Radar") -> "RADAr"
"""

def reverse(txt: str) -> str:
    return txt[::-1].swapcase()


if __name__ == "__main__":
    # Output from the function
    print(f"Result for 'Hello World': {reverse('Hello World')}")
    print(f"Result for 'ReVeRsE': {reverse('ReVeRsE')}")
    print(f"Result for 'Radar': {reverse('Radar')}")