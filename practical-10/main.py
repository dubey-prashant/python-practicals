import re

def check_string(s):
    # The pattern ^ (start of the string) and $ (end of the string)
    # are used to check the first and last character of the string.
    # The . (dot) matches any character except a newline.
    # The \1 is a backreference to the first group of the matched expression.
    pattern = r"^(.).*\1$"

    if re.match(pattern, s):
        return True
    else:
        return False

# Test the function
print(check_string("helloh"))  # Returns: True
print(check_string("python"))  # Returns: False
