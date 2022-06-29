# Priscilla Tham Ai Ching (ID: 28390121)
# 1.4 union.py


''' This function is designed to convert a table of integers into the form of a
matrix. '''
def convertToMatrix(list, line):
    for i in range(len(list)):

        if i != len(list) - 1:
            line += str(list[i]) + ' '

        else:
            line += str(list[i])

    return line

''' This function is designed to join the characters previously splitted after
completing necessary operations on the file. '''
def joinVertex(index, list, line):
    if index != (len(list) - 1):
        line += list[index] + ':'

    else:
        line += list[index]

    return line

''' This function is designed to combine the weights of the edges in two tables into one. '''
def combineEdges(table1, table2, indexList, index1, index2):
    table1[indexList[index1][1]][indexList[index2][1]] = table2[indexList[index1][0]][indexList[index2][0]]
    table1[indexList[index2][1]][indexList[index1][1]] = table2[indexList[index2][0]][indexList[index1][0]]

''' This function is designed to determine whether the values in table A is more than or less
than or equal to table B. The values in the main table is first replaced with the values
from table A. The values in the main table is then compared to the values in table B. Note
that comparison can only occur if neither of the table at the compared row and column is
equal to 0 because that indicates no such edge exist. It replaces the current values in the
main table with the table which has the lower value at that specific row and column.

argument: table1: this represents the main table for the final output.

argument: table2: this represents table B.

argument: indexList: this represents the list which consists of rows and
columns to be access in the table.

argument: index1: this represents the index of the items in indexList.

argument: index2: this represents the index of the items in indexList. This index is different
from index1.

returns: this function does not return anything.

There would also be:-
    + combineEdges
which have been omitted for conciseness. '''
def check(table1, table2, indexList, index1, index2):
    if table2[indexList[index1][0]][indexList[index2][0]] < table1[indexList[index1][1]][indexList[index2][1]]:

        if table2[indexList[index1][0]][indexList[index2][0]] != 0:
            combineEdges(table1, table2, indexList, index1, index2)

    elif table2[indexList[index1][0]][indexList[index2][0]] > table1[indexList[index1][1]][indexList[index2][1]]:

        if table1[indexList[index1][1]][indexList[index2][1]] == 0:
            combineEdges(table1, table2, indexList, index1, index2)

def appending(list, item):
    if item not in list:
        list.append(item)

''' This function is designed to get the index of the same item in list A and list B. It
appends the index of the item in list A and the index of the item in list B to list C.

argument: list1: this represents list A.

argument: list2: this represents list B.

argument: list3: this represents list C.

returns: this function does not return anything. '''
def getIndex(list1, list2, list3):
    for i in range(len(list1)):

        for j in range(len(list2)):

            if list1[i] == list2[j]:
                temp = []
                temp.append(i)
                temp.append(j)
                appending(list3, temp)

''' This function is designed to combine the items in two list into one. '''
def combineVertex(list1, list2):
    for i in range(len(list1)):
        appending(list2, list1[i])

def tabulate(table, list):
    for i in range(len(list)):
        table[i].append(list[i])

''' This function is designed to arrange each splitted lines into the table 
according to their respective row and column.

argument: content: this is the content of the input file which is splitted to
lines and further splitted to characters in each line.

argument: table: this is an empty table to be filled with values obtained from
the content.

returns: this function does not return anything.

There would also be:-
    + tabulate function
which have been omitted for conciseness. '''
def arrangeTable(content, table):
    for i in range(1, len(content.split('\n'))):
        weights = content.split('\n')[i].split(' ')
        tabulate(table, weights)


file1 = input('Please enter a file to open: ').strip('.txt')
file2 = input('Please enter a file to open: ').strip('.txt')

openFile1 = open(file1 + '.txt')
openFile2 = open(file2 + '.txt')

content1 = openFile1.read()
content2 = openFile2.read()

openFile1.close()
openFile2.close()

vertex1 = content1.split('\n')[0].split(':')
vertex2 = content2.split('\n')[0].split(':')

adjMat1 = [[] for rows in range(len(vertex1))]
adjMat2 = [[] for rows in range(len(vertex2))]

arrangeTable(content1, adjMat1)
arrangeTable(content2, adjMat2)

adjMat1 = [[int(i) for i in list] for list in adjMat1]
adjMat2 = [[int(i) for i in list] for list in adjMat2]

unionVertex = []

combineVertex(vertex1, unionVertex)
combineVertex(vertex2, unionVertex)

unionAdjMat = [[0 for i in range(len(unionVertex))] for list in range(len(unionVertex))]
unionIndex1 = []
# index of the same vertices in both file1 and unionVertex
unionIndex2 = []
# index of the same vertices in both file2 and unionVertex

getIndex(vertex1, unionVertex, unionIndex1)
getIndex(vertex2, unionVertex, unionIndex2)

for i in range(len(unionIndex1)):
    j = i + 1

    for j in range(len(unionIndex1)):
        combineEdges(unionAdjMat, adjMat1, unionIndex1, i, j)

for i in range(len(unionIndex2)):
    j = i + 1

    for j in range(len(unionIndex2)):
        check(unionAdjMat, adjMat2, unionIndex2, i, j)

file3 = open((file1 + '_or_' + file2 + '.txt'), 'w')

vertices = ''

for i in range(len(unionVertex)):
    vertices = joinVertex(i, unionVertex, vertices)

file3.write(vertices + '\n')
    
for i in range(len(unionAdjMat)):
        weighting = ''

        if i != (len(unionAdjMat) - 1):
            file3.write(convertToMatrix(unionAdjMat[i], weighting) + '\n')

        else:
            file3.write(convertToMatrix(unionAdjMat[i], weighting))

file3.close()
