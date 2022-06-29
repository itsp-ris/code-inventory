# Priscilla Tham Ai Ching (ID: 28390121)
# 2.3.1 greedy.py


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

''' This function is designed to check the connection of graph A to graph B via an
intermediate graph. It checks the existence of path from the first vertex to the last vertex.

argument: start: this represents the first vertex.

argument: end: this represents the last vertex.

argument: graph: this represents the list of vertex which each particular vertex is
connected to.

argument: path: this represents the list of visited vertex via an edge connecting
between them.

argument: checkpoint: this represents the previous visited vertex before the current one.

returns: this function returns whether the first vertex is connected to the last vertex. '''
def connectionCheck(start, end, graph, path, checkpoint):
    path += [start]

    if start == end:
        return 'graph IS connected'
        
    elif start == checkpoint:
        for i in range(len(graph[checkpoint])):

            if graph[checkpoint][i] in path:

                if i == len(graph[checkpoint]) - 1:
                    
                    if pathway != 'graph IS connected':
                        return 'graph IS NOT connected'
                    
                    else:
                        return pathway
                    
            else:
                pathway = connectionCheck(graph[checkpoint][i], end, graph, path, start)

    else:
        for vertex in graph[start]:

            if vertex not in path:
                pathway = connectionCheck(vertex, end, graph, path, start)
            
                if pathway == 'graph IS connected':
                    return pathway
                
        return checkpoint

''' This function is designed to generate all the paths connecting graph A to graph B via an
intermediate graph. It chooses the cheapest edge connecting the next vertex with the current
starting vertex.

argument: start: this represents the first vertex.

argument: graph: this represents the list of vertex with each particular vertex is
connected to.

argument: path: this represents the list of visited vertex via an edge connecting
between them.

argument: pathList: this represents the list of possible paths.

argument: endVertices: the list of possible last vertex.

returns: this function does not return anything. '''
def makePath(start, graph, path, pathList, endVertices):
    path += [start]

    if start in endVertices:
        pathList.append(path)
        #return 'graph IS connected'

    else:

        for vertex in graph[start]:

            if vertex not in path:
                return makePath(vertex, graph, path, pathList, endVertices)

        #return 'graph IS NOT connected'

''' This function is designed to sort the list in ascending order. '''
def selectionSort(list):
    for i in range(len(list)):
        min = i

        for j in range(i + 1, len(list)):

            if list[j][0] < list[min][0]:
                min = j

        temp = list[i]
        list[i] = list[min]
        list[min] = temp

    return list

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

def appending(list, item):
    if item not in list:
        list.append(item)

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
def check1(list1, list2, item1, item2, listindex1, listindex2):
    if list1[item1] == list2[item2]:
        appending(listindex1, item1)
        appending(listindex2, item2)
        return list1[item1]

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
    file4 = open(('greedy' + graph1 + intermediateGraph + graph2 + '.txt'), 'w')

    file4.close()

    file5 = open(('greedy' + graph1 + intermediateGraph + graph2 + 'connectivity.txt'), 'w')

    file5.close()

    file6 = open(('greedy' + graph1 + intermediateGraph + graph2 + 'cost.txt'), 'w')

    file6.close()

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

    graphConnection1 = {}

    for i in range(vertex4.index(intermediateVertex[0]), vertex4.index(graph2Vertex[-1])):
        edgeWeights = []

        for j in range(vertex4.index(intermediateVertex[0]), vertex4.index(graph2Vertex[-1])):

            if adjMat4[i][j] > 0:
                temp = []
                temp.append(adjMat4[i][j])
                temp.append(j)
                appending(edgeWeights, temp)

        edgeWeights = selectionSort(edgeWeights)

        for k in range(len(edgeWeights)):
            graphConnection1.setdefault(vertex4[i], []).append(vertex4[edgeWeights[k][1]])
    
    graphConnection2 = {}

    for i in range(len(vertex4)):

        for j in range(len(vertex4)):

            if adjMat4[i][j] > 0:
                graphConnection2.setdefault(vertex4[i], []).append(vertex4[j])

    pathList = []

    for i in range(len(intermediateVertex)):
        path = []

        if intermediateVertex[i] in graph1Vertex:
            makePath(intermediateVertex[i], graphConnection1, path, pathList, graph2Vertex)

    pathIndex = [] # index of visited vertex in path in pathList

    for i in range(len(pathList)):
        temp = []

        for j in range(len(pathList[i])):

            for k in range(len(vertex4)):

                if pathList[i][j] == vertex4[k]:
                    temp.append(k)

        appending(pathIndex, temp)

    cost = []

    for i in range(len(pathIndex)):
        total = 0

        for j in range(len(pathIndex[i])):

            if (j + 1) in range(len(pathIndex[i])):
                total += adjMat4[pathIndex[i][j]][pathIndex[i][j + 1]]

        cost.append(total)

    cheapestPath = pathList[cost.index(min(cost))]

    newVertex = []

    combineVertex(graph1Vertex, newVertex)
    combineVertex(intermediateVertex, newVertex)
    combineVertex(graph2Vertex, newVertex)

    newAdjMat = [[0 for i in range(len(newVertex))] for list in range(len(newVertex))]
    newIndex = [] # index of the same vertices in both vertex4 and newVertex

    for i in range(len(vertex4)):

        for j in range(len(newVertex)):

            if vertex4[i] == newVertex[j]:
                temp = []
                temp.append(i)
                temp.append(j)
                appending(newIndex, temp)

    for i in range(len(newIndex)):

        for j in range(len(newIndex)):

            if adjMat4[newIndex[i][0]][newIndex[j][0]] > 0:
                newAdjMat[newIndex[i][1]][newIndex[j][1]] = adjMat4[newIndex[i][0]][newIndex[j][0]]

    visited = []

    for i in range(len(newAdjMat)):

        for j in range(len(newAdjMat)):

            if (newVertex[i] in intermediateVertex) and (newVertex[j] in intermediateVertex):

                if (newVertex[i] in graph1Vertex) and (newVertex[j] in graph1Vertex):
                    pass

                elif (newVertex[i] in graph2Vertex) and (newVertex[j] in graph2Vertex):
                    pass

                else:
                    if ((newVertex[i] in cheapestPath) or (newVertex[j] in cheapestPath)) and not ((newVertex[i] in cheapestPath) and (newVertex[j] in cheapestPath)):
                        newAdjMat[i][j] = 0

                    else:
                        for k in range(len(cheapestPath)):
                            l = k + 1
                            m = k - 1

                            if (l in range(len(cheapestPath))) and (m in range(len(cheapestPath))):

                                if [newVertex[i], newVertex[j]] not in visited:

                                    if (((newVertex[i] == cheapestPath[k]) or (newVertex[j] == cheapestPath[l])) and not ((newVertex[i] == cheapestPath[k]) and (newVertex[j] == cheapestPath[l]))) and (((newVertex[i] == cheapestPath[m]) or (newVertex[j] == cheapestPath[k])) and not ((newVertex[i] == cheapestPath[m]) and (newVertex[j] == cheapestPath[k]))):
                                        newAdjMat[i][j] = 0
                                        newAdjMat[j][i] = 0

                                    elif ((newVertex[i] == cheapestPath[k]) and (newVertex[j] == cheapestPath[l])) and ((newVertex[i] == cheapestPath[m]) and (newVertex[j] == cheapestPath[k])):
                                        newAdjMat[j][i] = newAdjMat[i][j]
                                        temp = []
                                        temp.append(newVertex[i])
                                        temp.append(newVertex[j])
                                        visited.append(temp)
                                        temp = []
                                        temp.append(newVertex[j])
                                        temp.append(newVertex[i])
                                        visited.append(temp)

    file4 = open(('greedy' + graph1 + intermediateGraph + graph2 + '.txt'), 'w')

    vertices = ''

    for i in range(len(newVertex)):
        vertices = joinVertex(i, newVertex, vertices)

    file4.write(vertices + '\n')

    for i in range(len(newAdjMat)):
        weighting = ''

        if i != (len(newAdjMat) - 1):
            file4.write(convertToMatrix(newAdjMat[i], weighting) + '\n')

        else:
            file4.write(convertToMatrix(newAdjMat[i], weighting))

    file4.close()

    file5 = open(('greedy' + graph1 + intermediateGraph + graph2 + 'connectivity.txt'), 'w')

    file5.write(connectionCheck(newVertex[0], newVertex[-1], graphConnection2, path, newVertex[0]))

    file5.close()

    file6 = open(('greedy' + graph1 + intermediateGraph + graph2 + 'pathcost.txt'), 'w')

    file6.write(str(min(cost)))

    file6.close()
