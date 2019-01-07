#function named collatz() that has one parameter named number. 
# If number is even, then collatz() should print number // 2 and return this value.
# If number is odd, then collatz() should print and return 3 * number + 1.

def Collatz(number):
    if number % 2 == 0:
        RETNUM = number/2
        print(RETNUM) 
    else:
        RETNUM = 3 * number + 1
        print(RETNUM)
        
    return RETNUM

print('Hello, this is the collatz function')
print('Please enter a number')
NUM = int(raw_input('> '))


while NUM != 1:
    NUM = Collatz(NUM)









