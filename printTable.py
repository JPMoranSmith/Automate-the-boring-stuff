#! python3
# printTable.py - takes a list of data and prints into a table

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(data):
        colWidth = [0] * len(data)
        for i in range(4):
                for n in range(len(data)):
                        if colWidth[n] == 0:
                                colWidth[n] = len(max(data[n], key=len))
                        print (data[n][i].rjust(colWidth[n]) + ' |'),
                print
        
printTable(tableData)

