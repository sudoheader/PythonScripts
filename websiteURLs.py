#! python3

# Find website URLs that begin with http:// or https://

import re, pyperclip

# TODO: Return list of URLs that match the regex

urlRegex = re.compile(r'''
^    # starting anchor
([http://]+)    # match strings that begin with http://
([https://]+)   # match strings that begin with https://
([.*{2,5}]+)
$    # ending anchor
''', re.VERBOSE)

# TODO: Figure out if there are any clipboard matches with regex

urls = pyperclip.paste()

extractedURLs = urlRegex.findall(urls)

allURLs = []
for urls in extractedURLs:
    allURLs.append(urls[0])

# Copy the extracted email/phone to the clipboard
results = ','.join(allURLs) + '\n'
pyperclip.copy(results)
