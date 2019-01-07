""" Multi line comments can be done using the three 
quote marks in your code.

"""
print('Hello I\'m using an escape char') # use of \ to escape '
"""
Escape character
\' Single quote
\" Double quote
\t Tab
\n Newline (line break)
\\ Backslash 
"""
# raw strings, ignores all escape characters and prints any backslash that appears in the string
print(r'That is Carol\'s cat.')

# multiline strings using '''
print('''Dear Me,

Try to do more constructive things,
instead of gaming!

JMS''')

# Strings use indexes and slices the same way lists do.

spam = 'Hello World!'
print(spam)

print(spam[1]) # indexing

print(spam[0:5])    #slicing
print(spam[:5])
print(spam[6:])     #slicing

# In and Not in operators

if 'Hello' in spam: # is 'Hello in spam?
    print('YES!')
else:
    print('NO!')

if 'Hello' not in spam:
    print('It is not in')
else:
    print('It is in!')

# The upper(), lower(), isupper(), and islower() String Methods

spam = 'Hello to you!'
print('This is spam.upper() %s' %spam.upper())
print('This is spam.lower() %s' %spam.lower())

# The join() and split() String Methods
spam = ', '
newList = ['cats', 'bats', 'rats']
print(spam.join(newList))           # join() is called on a string value and is passed a list value, lsit must contain strings to work

newList = 'My name is Simon'.split()    # creates list of strings delimited on space chars, can pass in strings to split on