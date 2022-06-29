# Priscilla Tham Ai Ching (ID: 28390121)
# 1.1 graphFileOps.py


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
        tabulate(adjMat, weights)
        

file = open(input('Please enter a file to open: '))

content = file.read()

file.close()

vertex = content.split('\n')[0].split(':')

adjMat = [[] for rows in range(len(vertex))]

arrangeTable(content, adjMat)

# 1.2 graphFileOps.py

file2 = open((input('Please enter new file name: ')), 'w')

vertices = ''

for i in range(len(vertex)):
    vertices = joinVertex(i, vertex, vertices)

file2.write(vertices + '\n')
    
for i in range(len(adjMat)):
    weighting = ''
    file2.write(convertToMatrix(adjMat[i], weighting) + '\n')

file2.close()
