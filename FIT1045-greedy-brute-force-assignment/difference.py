# Priscilla Tham Ai Ching (ID: 28390121)
# 1.5 difference.py


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

    for j in range(len(unionIndex1)):
        combineEdges(unionAdjMat, adjMat1, unionIndex1, i, j)

for i in range(len(unionIndex2)):

    for j in range(len(unionIndex2)):

        if adjMat2[unionIndex2[i][0]][unionIndex2[j][0]] < unionAdjMat[unionIndex2[i][1]][unionIndex2[j][1]]:

            if adjMat2[unionIndex2[i][0]][unionIndex2[j][0]] != 0:
                unionAdjMat[unionIndex2[i][1]][unionIndex2[j][1]] = 0

        elif adjMat2[unionIndex2[i][0]][unionIndex2[j][0]] > unionAdjMat[unionIndex2[i][1]][unionIndex2[j][1]]:

            if unionAdjMat[unionIndex2[i][1]][unionIndex2[j][1]] == 0:
                combineEdges(unionAdjMat, adjMat2, unionIndex2, i, j) 

            else:
                unionAdjMat[unionIndex2[i][1]][unionIndex2[j][1]] = 0

        elif vertex2[unionIndex2[i][0]] in intersectingVertex:

            if vertex2[unionIndex2[j][0]] in intersectingVertex:

                if adjMat2[unionIndex2[i][0]][unionIndex2[j][0]] == unionAdjMat[unionIndex2[i][1]][unionIndex2[j][1]]:
                    unionAdjMat[unionIndex2[i][1]][unionIndex2[j][1]] = 0

toRemove = [0 for i in range(len(unionVertex))]
# an array of 0s indicating vertex with no connection to any other vertex
toRemoveIndex = []
# index of the array of 0s in unionAdjMat
newVertex = []
newAdjMat = []

for i in unionAdjMat:

    if i != toRemove:
        appending(newVertex, unionVertex[unionAdjMat.index(i)])
        appending(newAdjMat, i)

    else:
        appending(toRemoveIndex, unionAdjMat.index(i))

for i in range(len(newAdjMat)):

    for j in range(len(toRemoveIndex)):
        newAdjMat[i].remove(newAdjMat[i][toRemoveIndex[j]])

file3 = open((file1 + '_xor_' + file2 + '.txt'), 'w')

vertices = ''

for i in range(len(newVertex)):
    vertices = joinVertex(i, newVertex, vertices)

file3.write(vertices + '\n')

for i in range(len(newAdjMat)):
        weighting = ''

        if i != (len(newAdjMat) - 1):
            file3.write(convertToMatrix(newAdjMat[i], weighting) + '\n')

        else:
            file3.write(convertToMatrix(newAdjMat[i], weighting))

file3.close()
