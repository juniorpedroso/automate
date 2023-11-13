def maxStr(thisList):
    max = 0
    for i in range(len(thisList)):
        if max < len(thisList[i]):
            max = len(thisList[i])
    return max + 1


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


colWidth = []
for i in range(len(tableData)):
    max = maxStr(tableData[i])
    colWidth.append(max)

nLine = len(tableData[0])   # 4 Lines
nCol = len(tableData)       # 3 Collumns

for l in range(nLine):
    for c in range(nCol):
        print(tableData[c][l].rjust(colWidth[c]), end='')
    print()

print()
