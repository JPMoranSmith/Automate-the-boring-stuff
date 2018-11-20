#! python 2.7
# regexDuplicate.py
# search text strings for duplciate consecutive words

import re, pyperclip

dup = re.compile(r'\b(\w+)\s+\1\b|(\W+)\s*\2') # looks for consectuive words (\w+)\1 is referencing group 1 
matches = []

inText = pyperclip.paste()

for i in dup.findall(inText):
	for j in i:
		if j <> '':
			matches.append(j)

print matches
