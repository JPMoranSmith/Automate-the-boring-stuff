#! python 2.7
# pw.py - an insecure password locker program

# sample data for testing
PASSWORDS = {'email': 'F1234xcfwr',
             'blog': 'Blog123!xx',
             'luggage': '1234'}

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]   # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
