numList = [1, 2, 3] # lists are defined with []

print(numList) #prints the list

#lists can have any types inside them
mixedList = [1, 'cat', 3.1415, True, None, 'bye']

#Lists are indexed
print 'indexing a list'
print mixedList
print 'mixedlist[1] is'
print(mixedList[1]) # prints 'cat'
print 'mixedlist[-1] is'
print(mixedList[-1]) # prints 'bye'

#lists within a list
spam = [['cat', 'bat'], [10,20,30,40]]
print(spam[0])  #prints ['cat', 'bat']
print(spam[0][1]) # prints bat
print(spam[1][3]) # prints 40

#Getting Sublists with Slices
spam = ['cat', 'bat', 'rat', 'hat']
print(spam[0])  #is a list with an index
print(spam[0:3]) #is a list with a slice (3 integers)
print(spam[1:3]) # two integers notice second integer is where slice ends!
print(spam[0:-1]) # prints cat, bat, rat

# can leave either integer off slice
print(spam[:2]) # from start of list to length of list
print(spam[2:]) # from index 2 to length of list

#can itterate over a list
for num in range(len(mixedList)):
    print(mixedList[num])

#changing values in a list
spam = ['cat', 'bat', 'rat', 'hat']
spam[1] = 'aadvark'
print(spam)
spam[2] = spam[1]
spam[-1] = 12345
print(spam)

#list concatenation and replciation 
spam = [1, 2, 3]
spam = spam + ['A', 'B', 'C']
print(spam)
spam = spam * 3 
print(spam)

#deleting values from a list
spam = ['cat', 'bat', 'rat', 'hat', 'elephant']
del spam[2]
print(spam) #notice values after deleted item move down one index

del [spam[1:3]] #can also del using a slice!
print(spam)

#in and not in a list
boolAnimals = 'cat' in spam
print(boolAnimals) # prints true
boolAnimals = 'urMum' in spam # this is false
print(boolAnimals)

#multiple assignment trick
cat = ['fat', 'orange', 'loud']
size, colour, disposition = cat
print 'My cat is ' + size + ', ' + colour + ' and ' + disposition

# List methods

#find a value in a list with index()
spam = ['hello', 'hi', 'howdy', 'heyas', 'hello']
greetIndex = spam.index('hello') #returns 0, 1st appearnace
print greetIndex
greetIndex = spam.index('heyas') #returns 3
print greetIndex

# adding values to a list
spam.append('Yo') #adds to the end of the list
print spam
spam.insert(1, 'Bonjour') #insert into index 1 and move all others along
print spam

# remove values from a list
print 'Before we remove something :'
print spam
spam.remove('Bonjour') # removes from the list
print 'After we remove something :'
print spam

# sorting values in a list with sort()
sizes =[2, 5, 3.14, 1, -7]
animals = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
print 'Before sorting :'
print sizes
print animals
sizes.sort()    # sort numerically
animals.sort()  # sort alphabetically
print 'After sorting :'
print sizes
print animals

# can do reverse sort
sizes.sort(reverse=True)
print 'Can reverse sort too :'
print sizes

# cant sort mixed lists!
# sort uses ASCIIbetical order, uppercase comes before lower
spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
print spam
print 'Now sort :'
spam.sort()
print spam
print 'Now sort using argument str.lower :'
spam.sort(key=str.lower)
print spam

# tuples typed with ()
# like lists but are immutable
eggs = ('hello', 1, 2)
print eggs
print type(eggs)

# convert between lists and tuples
neweggs = list(eggs)
print neweggs
print type(neweggs)

# references
print 'Assigning a list ot avariable, you are actually asigning a reference'
spam = [0, 1, 2, 3]
print 'Spam is: '
print spam
cheese = spam
print 'cheese is:'
print cheese
print 'Now change Cheese[1]'
cheese[1] = 'Hello'
print spam
print cheese
print 'Both spam and cheese have changed!'

# copy and deepcopy 
import copy

spam = ['A', 'B', 'C', 'D']
print 'List to copy is spam'
print spam
cheese = copy.copy(spam)
print 'copy spam to cheese :'
print cheese
cheese[1] = 42
print 'now change cheese[1] to 42 and print spam and cheese'
print spam
print cheese
print 'If you ned to copy a list within a list use deepcopy()'




