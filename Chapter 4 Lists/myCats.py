# gets names from user input and puts
# them into a list and prints them out

myCats = []
while True:
    print('Enter the name of cat ' + str(len(myCats) + 1) + ' (Or nothing to stop.):')
    name = raw_input('> ')
    if name == '':
        break
    elif name in myCats:
        print('That cat has already been entered!')
    else:
        myCats = myCats + [name] #list concatentation
    
print('The cat names are:')
for name in myCats:
    print(' ' + name)