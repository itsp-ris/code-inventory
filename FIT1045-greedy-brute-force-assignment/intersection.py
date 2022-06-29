# Priscilla Tham Ai Ching (ID: 28390121)
# 1.3 intersection.py


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
        line += list[i] + ':'

    else:
        line += list[i]

    return line

''' This function is designed to determine whether the values in table A
is either more than or less than or equal to the values in table B at a
specific row and column. It replaces the current values in table C with
the table which has the higher value at that specific row and column.

argument: table1: this represents table A.

argument: table2: this represents table B.

argument: table3: this represents the main table for the final output.

argument: indexList1: this represents the list which consists of rows and
columns to be access in the table1.

argument: indexList2: this represents the list which consists of rows and
columns to be access in the table2.

argument: index1: this represents the index of the items in indexList.

argument: index2: this represents the index of the items in indexList. This index is different
from index1.

returns: this function does not return anything. '''
def check3(table1, table2, table3, indexList1, indexList2, index1, index2):
    if table2[indexList2[index1]][indexList2[index2]] > table1[indexList1[index1]][indexList1[index2]]:
        table3[index1][index2] = table2[indexList2[index1]][indexList2[index2]]
        table3[index2][index1] = table2[indexList2[index2]][indexList2[index1]]

    else:
        table3[index1][index2] = table1[indexList1[index1]][indexList1[index2]]
        table3[index2][index1] = table1[indexList1[index2]][indexList1[index1]]

def appending(list, item):
    if item not in list:
        list.append(item)

''' This function is designed to determine whether the values in the table
of a specific row and column is more than 0. It appends the index of those
values to another list.

argument: table: this represents the table to be assess.

argument: indexList: this represents the list which consists of rows and
columns to be access in the table.

argument: list: this represents the list to be appended with the index of
those rows and columns which values are more than 0.

returns: this function does not return anything.

There would also be:-
    + appending function
which have been omitted for conciseness. '''
def check2(table, indexList, list):
    for i in range(len(indexList)):

        for j in range(len(indexList)):

            if table[indexList[i]][indexList[j]] > 0:
                appending(list, indexList[i])
                appending(list, indexList[j])

''' This function is designed to determine if item in list A at a specific index
and item in list B at a specific index is the same. It appends to another list
which corresponds to list A the index of the item in list A and appends to another
list which corresponds to list B the index of the item in list B given that they
are the same.

argument: list1: this represents list A.

argument: list2: this represents list B.

argument: index1: this represents the specific index of the item to be referred in
list A.

argument: index2: this represents the specific index of the item to be referred in
list B.

argument: indexList1: this represents the list which corresponds to list A to be
appended with the index of the item given that it is equal to the item in list B
at the specific index.

argument: indexList2: this represents the list which corresponds to list B to be
appended with the index of the item given that it is equal to the item in list A
at the specific index.

returns: this function returns the item of list A at the specific index.

There would also be:-
    + appending function
which have been omitted for conciseness. '''
def check1(list1, list2, index1, index2, indexList1, indexList2):
    if list1[index1] == list2[index2]:
        appending(indexList1, index1)
        appending(indexList2, index2)
        return list1[index1]

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

vertexIndex1 = [] # index of vertices in file1 which is also in file2
vertexIndex2 = [] # index of vertices in file2 which is also in file1

edges1 = []
# index of vertices which has an edge connecting to each other between vertices in vertexIndex1 
edges2 = []
# index of vertices which has an edge connecting to each other between vertices in vertexIndex2

for i in range(len(vertex1)):

    for j in range(len(vertex2)):
        check1(vertex1, vertex2, i, j, vertexIndex1, vertexIndex2)

check2(adjMat1, vertexIndex1, edges1)
check2(adjMat2, vertexIndex2, edges2)

intersectingVertex = []
intersectingIndex1 = []
# index of vertices in file1 which intersects with vertices and edges in file2
intersectingIndex2 = []
# index of vertices in file2 which intersects with vertices and edges in file1

for i in range(len(edges1)):
    
    for j in range(len(edges2)):
        response = check1(vertex1, vertex2, edges1[i], edges2[j], intersectingIndex1, intersectingIndex2)

        if response != None:
            appending(intersectingVertex, response)

intersectingEdges = [[0 for i in range(len(intersectingVertex))] for rows in range(len(intersectingVertex))]

for i in range(len(intersectingEdges)):
    
    for j in range(len(intersectingEdges)):
        check3(adjMat1, adjMat2, intersectingEdges, intersectingIndex1, intersectingIndex2, i, j)       

file3 = open((file1 + '_and_' + file2 + '.txt'), 'w')

vertices = ''

for i in range(len(intersectingVertex)):
    vertices = joinVertex(i, intersectingVertex, vertices)

file3.write(vertices + '\n')
    
for i in range(len(intersectingEdges)):
        weighting = ''

        if i != (len(intersectingEdges) - 1):
            file3.write(convertToMatrix(intersectingEdges[i], weighting) + '\n')

        else:
            file3.write(convertToMatrix(intersectingEdges[i], weighting))

file3.close()
