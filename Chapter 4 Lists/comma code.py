# A cuntion tha takes a list value
# as an argument and returns a string
# with all items separated by a comma and
# a space with and inserted before the last item

def commacode(inList):
    outString = ''
    for i in inList:
        if inList.index(i) < (len(inList) -1):
            outString += str(i) + ', '
        else:
            outString += 'and ' + str(i)
    return(outString)


spam = ['apples', 'bananas', 'tofu', 'cats']
print commacode(spam)

spam = [1, 2, 3, 4, 5, 6 ,'Hello!', 0.23]
print commacode(spam)