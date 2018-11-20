#! python 2.7
# -*- coding: cp1252 -*-
# regexStrip.py
# a function that takes a string and does the same thing
# as the strip() string method. If no other arguments are passed other
# than the string to strip, then whitespace characters will be removed
# from the beginning and end of the string. Otherwise, the characters
# specified in the second argument to the function will be removed from
# the string.
# 
'''
REG EX explanation
'\s*        # 0 or more empty spaces
[{s}]*      # 0 or more matches of char s
(.*?)       # group 1
[{s}]*      # 0 or more matches of char s
\s*
$'
.format(s=x)
'''

import re

def stripCustom(text, x=' '):
    # set x as ' ' if nothing passed into function
    # returns the group1 that is matched by the regex
    return re.search('\s*[{s}]*(.*?)[{s}]*\s*$'.format(s=x), text).group(1)

