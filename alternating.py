#! python3

import pyperclip, sys

text = pyperclip.paste()

alt_case = lambda s : ''.join([c.upper() if c.islower() else c.lower() for c in s])
print(alt_case(text))