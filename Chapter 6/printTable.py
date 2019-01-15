#! python3
# printTable.py - takes a list of data and prints into a table

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David', 'Jerry', 'Brian'],
             ['dogs', 'cats', 'moose', 'goose', 'cricket']]

def printTable(data):
        maxLen = len(max(data, key=len))
        colWidth = [0] * len(data)
        for i in range(maxLen):
                for n in range(len(data)):
                        if colWidth[n] == 0:
                                colWidth[n] = len(max(data[n], key=len))
                        try:
                                print (data[n][i].rjust(colWidth[n]) + ' |', end='')
                        except IndexError:
                                print ('NULL'.rjust(colWidth[n]) + ' |', end='')
                print()
        
printTable(tableData)



