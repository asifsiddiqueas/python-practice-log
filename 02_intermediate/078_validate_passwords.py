import re

def validate_passwords(password_sequence):
    """Validate comma-separated passwords against complexity rules (len 6-12, upper, lower, num, special)."""
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