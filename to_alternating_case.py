#! python3
import pyperclip, sys

text = pyperclip.paste()

#if text != None:
 #   to_alternating_case(text)
#
#   text = input('Enter the string to swap here: ')
    
# print(sys.argv)

# From https://stackoverflow.com/a/36247302
def to_alternating_case(string):
    temp = ""
    for character in string:
        if character.isupper() == True:
            temp += character.lower()
        else:
            temp += character.upper()
    return temp
    
to_alternating_case(text)