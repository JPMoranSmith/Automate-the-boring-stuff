# Automate The Boring Stuff 
# https://automatetheboringstuff.com/chapter3/
# Functions
# Error handling

def spam(divideBy):  # define function spam 
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))