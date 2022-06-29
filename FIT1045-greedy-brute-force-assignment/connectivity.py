# Priscilla Tham Ai Ching (ID: 28390121)
# 2.2 connectivity.py


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

file = input('Please enter a file to open: ').strip('.txt')

openFile = open(file + '.txt')

content = openFile.read()

openFile.close()

vertex = content.split('\n')[0].split(':')

adjMat = [[] for rows in range(len(vertex))]

arrangeTable(content, adjMat)

adjMat = [[int(i) for i in list] for list in adjMat]

graph = {}

for i in range(len(adjMat)):

    for j in range(len(adjMat[i])):

        if adjMat[i][j] > 0:
            graph.setdefault(vertex[i], []).append(vertex[j])

path = []

file2 = open((file + 'connectivity.txt'), 'w')

file2.write(connectionCheck(vertex[0], vertex[-1], graph, path, vertex[0]))

file2.close()
