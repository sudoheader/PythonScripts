#! python3

# Write a function that takes a string and does the same thing as the strip()
# string method. If no other arguments are passed other than the string to
# strip, then whitespace characters will be removed from the beginning and
# end of the string. Otherwise, the characters specified in the second
# argument to the function will be removed from the string.

import re

def strip(s, chars=None):
    if chars is None:
        print(re.sub(r'^\s*(.*?)\s*$', r'\1', s))

strip('test', 's')
