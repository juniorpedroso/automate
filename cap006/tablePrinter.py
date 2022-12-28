tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    nCol = len(table) # Verifica o número de colunas

    wCol = []
    for n in range(nCol):
        width = 0
        for line in range(len(table[n])):
            newWidth = len(table[n][line])
            if newWidth > width:
                width = newWidth
        wCol.append(width)
    
    for lines in range(len(wCol) + 1):
        for columns in range(nCol):
            print(table[columns][lines].rjust(wCol[columns]) + ' | ', end='')
        print()

printTable(tableData)