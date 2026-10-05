"""
Python program to create a function that computes the Hamming distance between two strings.
Hamming distance is the number of characters that differ between two strings.

Examples:
    hamming_distance("abcde", "bcdef") -> 5
    hamming_distance("abcde", "abcde") -> 0
    hamming_distance("strong", "strung") -> 1
"""

def hamming_distance(str1: str, str2: str) -> int:
    return sum(1 for c1, c2 in zip(str1, str2) if c1 != c2)


if __name__ == "__main__":
    # Output from the function
    print(f"Distance for 'abcde' and 'bcdef': {hamming_distance('abcde', 'bcdef')}")
    print(f"Distance for 'abcde' and 'abcde': {hamming_distance('abcde', 'abcde')}")
    print(f"Distance for 'strong' and 'strung': {hamming_distance('strong', 'strung')}")