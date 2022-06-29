# Priscilla Tham Ai Ching (ID: 28390121)
# 2.1 supergraph.py


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
def check2(table1, table2, indexList, index1, index2):
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

''' This function is designed to check if an intermediate graph exist amongst
the input file. It checks if one of the graph has shared vertices and edges with
the other two graphs given that the two graphs had no shared vertices and edges
with each other.

argument: list1: this represents the vertices in graph A.

argument: list2: this represents the vertices in graph B.

argument: list3: this represents the vertices in graph C.

returns: this function returns whether the intermediate graph exist. '''
def intermediateCheck(list1, list2, list3):
    vertexIndex1 = []
    vertexIndex2 = []
    vertexIndex3 = []
    
    for i in range(len(list1)):

        for j in range(len(list3)):
            check1(list1, list3, i, j, vertexIndex1, vertexIndex3)

    for i in range(len(list2)):

        for j in range(len(list3)):
            check1(list2, list3, i, j, vertexIndex2, vertexIndex3)

    if (len(vertexIndex1) > 0) and (len(vertexIndex2) > 0) and (len(vertexIndex3) > 0):
        return True

    else:
        return False

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
file3 = input('Please enter a file to open: ').strip('.txt')

openFile1 = open(file1 + '.txt')
openFile2 = open(file2 + '.txt')
openFile3 = open(file3 + '.txt')

content1 = openFile1.read()
content2 = openFile2.read()
content3 = openFile3.read()

openFile1.close()
openFile2.close()
openFile3.close()

vertex1 = content1.split('\n')[0].split(':')
vertex2 = content2.split('\n')[0].split(':')
vertex3 = content3.split('\n')[0].split(':')

adjMat1 = [[] for rows in range(len(vertex1))]
adjMat2 = [[] for rows in range(len(vertex2))]
adjMat3 = [[] for rows in range(len(vertex3))]

arrangeTable(content1, adjMat1)
arrangeTable(content2, adjMat2)
arrangeTable(content3, adjMat3)

adjMat1 = [[int(i) for i in list] for list in adjMat1]
adjMat2 = [[int(i) for i in list] for list in adjMat2]
adjMat3 = [[int(i) for i in list] for list in adjMat3]

graphs = [file1, file2, file3]

result = []

result.append(intermediateCheck(vertex3, vertex2, vertex1))
result.append(intermediateCheck(vertex1, vertex3, vertex2))
result.append(intermediateCheck(vertex2, vertex1, vertex3))

response = 'True'

if False in result:
    intermediateGraph = graphs[result.index(True)]

    if result.index(True) == 0:
        graph1 = graphs[1]
        graph1Vertex = vertex2
        graph1AdjMat = adjMat2
        graph2 = graphs[2]
        graph2Vertex = vertex3
        graph2AdjMat = adjMat3
        intermediateVertex = vertex1
        intermediateAdjMat = adjMat1

    elif result.index(True) == 1:
        graph1 = graphs[0]
        graph1Vertex = vertex1
        graph1AdjMat = adjMat1
        graph2 = graphs[2]
        graph2Vertex = vertex3
        graph2AdjMat = adjMat3
        intermediateVertex = vertex2
        intermediateAdjMat = adjMat2

    else:
        graph1 = graphs[0]
        graph1Vertex = vertex1
        graph1AdjMat = adjMat1
        graph2 = graphs[1]
        graph2Vertex = vertex2
        graph2AdjMat = adjMat2
        intermediateVertex = vertex3
        intermediateAdjMat = adjMat3

else:
    response = 'Intermediate graph does not exist'

if response != 'True':
    file4 = open(('supergraph' + graph1 + intermediateGraph + graph2 + '.txt'), 'w')

    file4.write(response)

    file4.close()

else:
    vertex4 = []

    combineVertex(graph1Vertex, vertex4)
    combineVertex(intermediateVertex, vertex4)
    combineVertex(graph2Vertex, vertex4)

    adjMat4 = [[0 for i in range(len(vertex4))] for list in range(len(vertex4))]
    vertexIndex1 = [] # index of the same vertices in both graph1Vertex and vertex4
    vertexIndex2 = [] # index of the same vertices in both graph2Vertex and vertex4
    vertexIndex3 = [] # index of the same vertices in both intermediateGraph and vertex4

    getIndex(graph1Vertex, vertex4, vertexIndex1)
    getIndex(intermediateVertex, vertex4, vertexIndex3)
    getIndex(graph2Vertex, vertex4, vertexIndex2)

    for i in range(len(vertexIndex1)):

        for j in range(len(vertexIndex1)):
            combineEdges(adjMat4, graph1AdjMat, vertexIndex1, i, j)

    for i in range(len(vertexIndex3)):

        for j in range(len(vertexIndex3)):
            check2(adjMat4, intermediateAdjMat, vertexIndex3, i, j)

    for i in range(len(vertexIndex2)):

        for j in range(len(vertexIndex2)):
            check2(adjMat4, graph2AdjMat, vertexIndex2, i, j)

    file4 = open(('supergraph' + graph1 + intermediateGraph + graph2 + '.txt'), 'w')

    vertices = ''

    for i in range(len(vertex4)):
        vertices = joinVertex(i, vertex4, vertices)

    file4.write(vertices + '\n')

    for i in range(len(adjMat4)):
        weighting = ''

        if i != (len(adjMat4) - 1):
            file4.write(convertToMatrix(adjMat4[i], weighting) + '\n')

        else:
            file4.write(convertToMatrix(adjMat4[i], weighting))

    file4.close()
