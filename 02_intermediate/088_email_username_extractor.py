"""
Extracts the username from an email address formatted as username@companyname.com.
Input: A string email address where both username and company are composed of letters.
Output: A string representing just the username.
"""

def extract_username(email_address):
    
    # split on '@' and return the leading segment
    return email_address.split('@')[0]

# test cases
if __name__ == "__main__":
    user_input = input("Enter an email address: ")
    
    username = extract_username(user_input)
    
    print(username)
    # expected output for sid@google.com: sid