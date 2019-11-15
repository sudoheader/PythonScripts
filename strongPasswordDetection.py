#! python3

import re, pyperclip

# Write a function that uses regular expressions to make sure the password
# string it is passed is strong. A strong password is defined as one that is
# at least eight characters long, contains both uppercase and lowercase
# characters, and has at least one digit. You may need to test the string
# against multiple regex patterns to validate its strength.

# TODO: Create regex for strong password detection
passwordRegex = re.compile(r'''
^              # beginning anchor 
(?=.*[a-zA-Z]  # contains both uppercase and lowercase chars
(?=.*[0-9])    # has at least 1 digit
.{8,}          # is at least 8 chars long
$              # ending anchor
''', re.VERBOSE)

# Get text off clipboard
password = pyperclip.paste()

# Extract password from text
strongPassword = passwordRegex.findall(password)

# Return true or false if password is strong
if password in strongPassword:
    print('True')
else:
    print('False')
