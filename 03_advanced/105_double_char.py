"""
Pyhon program to create a function that takes a string and returns a string in which each character is repeated once.

Examples:
    double_char("String") -> "SSttrriinngg"
    double_char("Hello World!") -> "HHeelllloo WWoorrlldd!!"
    double_char("1234! ") -> "11223344!!"
"""

def double_char(txt: str) -> str:
    return "".join(c * 2 for c in txt)


if __name__ == "__main__":
    # Output from the function
    print(f"Result for 'String': {double_char('String')}")
    print(f"Result for 'Hello World!': {double_char('Hello World!')}")
    print(f"Result for '1234! ': {double_char('1234! ')}")