"""
Python program to create a function that replaces all the vowels in a string with a specified character.

Examples:
    replace_vowels("the aardvark", "#") -> "th# ##rdv#rk"
    replace_vowels("minnie mouse", "?") -> "m?nn?? m??s?"
    replace_vowels("shakespeare", "*") -> "shkspr*"
"""

import re

def replace_vowels(txt: str, ch: str) -> str:
    return re.sub(r"[aeiouAEIOU]", ch, txt)


if __name__ == "__main__":
    # Output from the function
    print(f"Result for 'the aardvark': {replace_vowels('the aardvark', '#')}")
    print(f"Result for 'minnie mouse': {replace_vowels('minnie mouse', '?')}")
    print(f"Result for 'shakespeare': {replace_vowels('shakespeare', '*')}")