"""
Validates a comma-separated sequence of passwords against specific complexity criteria ([a-z], [A-Z], [0-9], [$#@], length 6-12).
Input: A comma-separated string of passwords (e.g., "ABd1234@1,a F1#,2w3E*,2We3345")
Output: A comma-separated string containing only the valid passwords (e.g., "ABd1234@1")
"""

import re

def validate_passwords(password_sequence):
    
    # lookaheads ensure all character sets are present, while .{6,12} enforces the length constraints
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@]).{6,12}$"
    
    # split, filter out the invalid ones, and re-join
    valid_passwords = [pwd for pwd in password_sequence.split(',') if re.match(pattern, pwd)]
    
    return ','.join(valid_passwords)

# test cases
input_data = "ABd1234@1,a F1#,2w3E*,2We3345"

processed_data = validate_passwords(input_data)

print(f"Original sequence: {input_data}")
print(f"Valid passwords:   {processed_data}")
# expected output: ABd1234@1