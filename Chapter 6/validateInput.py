''' Written for Python 2.7
Takes a user input and checks if the age is an integer and password is an alphanumeric string
'''

while True:
    print('Enter your age:')
    age = raw_input()
    try:
        int(age)
    except ValueError:
        print('Please enter a number for you age.')
    else:
        break                              

while True:
    print('Select a new password (letters and numbers only):')
    password = raw_input()
    if password.isalnum():
        break
    print('Passwords can only have letters and numbers.')

print('Your age and password are %s %s' %(age, password))
