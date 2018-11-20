#! python 2.7
# -*- coding: cp1252 -*-
# pwCheck.py - a password checker
# checks password entered has:
# At least 8 characters
# Contains both uppercase and lower case chars and at least 1 digit

import re

pwRegex = re.compile(r'''
            ^                   # Start anchor
            (?=.*[A-Z])         # Ensure string has 1+ uppercase letter.
            (?=.*\W)            # Ensure string has 1+ special case letter.
            (?=.*\d)            # Ensure string has 1+ digits.
            (?=.*[a-z])         # Ensure string has 1+ lowercase letters.
            .{8,}               # Ensure string is at least length 8.
            $                   # End anchor.
            ''', re.VERBOSE) 

def checkPW(password):
    # function to test input from user against strong password rule
    if pwRegex.match(password):
        print 'Password is strong!'
        return 1
    else:
        print 'You\'re password is not strong enough!'
        return 0

def main():
    # main function loop until strong password entered
    print '''
    Please enter a password that has the following:
        * At least 1 uppercase and 1 lowercase letter
        * At lease 1 digit
        * At least 1 character eg: !£$%^&*?@
    '''
    pwFlag = 0    
    while pwFlag == 0:
        pwFlag = checkPW(raw_input('Enter a password: '))

main()
    
