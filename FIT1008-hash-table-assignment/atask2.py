''''
ID: 28390121
author: Priscilla Tham
Date: 15.05.2018
'''
# from atask1 import HashTable
# from atask3 import HashTableLinear as HashTable
from atask4 import HashTableQuadratic as HashTable
import timeit


def open_file(filename):
    '''
    functions opens and reads a file
    precondition: file exist in directory
    :param filename: the file the user wants to open and read
    postcondition:
    :return: lines of the file
    complexity: best and worst: O(1)
    '''
    with open(filename + '.txt', 'r', encoding='utf-8-sig') as file:
        content = file.read().strip()
    file.close()
    item = content.split('\n')
    return item


def time_inserting(content, table):
    '''
    functions calculates the time taken to insert the content of the file into the hash table
    precondition:
    :param content: every line in the file is a (key, value) pair to be inserted into the hash table

    postcondition: hash table is not empty
    :return: time taken
    complexity: best: O(1) when there is only one (key, value) pair to be inserted
                worst: O(N) where N is the number of lines representing the (key, value) pair to be inserted
    '''
    start = timeit.default_timer()
    for i in range(len(content)):
        table[content[i]] = content[i]
    taken = timeit.default_timer() - start
    return taken


def write_file(data):
    '''
    functions opens and writes or appends into a file
    precondition:
    :param data: the content to be written into the file
    postcondition: file exist in the directory and is not empty
    :return:
    complexity: best and worst: O(1)
    '''
    with open('csvfile.csv', 'a') as file:
        file.write(data)
    file.close()


if __name__ == '__main__':
    #210000, 209987, 400000 and 399989 and 202361.
    filename = input('Enter filename: ')
    for i in range(5):
        base = int(input('Enter base: '))
        content = open_file(filename)
        size = [400000, 399989, 210000, 209987, 202361]
        for j in range(5):
            table = HashTable(size[j], base)
            time_taken = time_inserting(content, table)
            avg_probeLength = table.probe_length/table.count
            data = str(size[j]) + ', ' + str(time_taken) + ', ' + str(table.collision) + ', ' + str(
                avg_probeLength) + '\n'
            write_file(data)

    '''filename = input('Enter filename: ')
    for i in range(5):
        base = int(input('Enter base: '))
        content = open_file(filename)
        size = [400000, 399989, 210000, 209987, 202361]
        for j in range(5):
            table = HashTable(size[j], base)
            time_taken = time_inserting(content, table)
            #avg_probeLength = table.probe_length / table.count
            data = str(size[j]) + ', ' + str(time_taken) + '\n' #+ ', ' + str(table.collision) + ', ' + str(
                #table.track_avg_probe_length()) + '\n'
            write_file(data)

    filename = input('Enter filename: ')
    for i in range(5):
        base = int(input('Enter base: '))
        content = open_file(filename)
        size = [400000, 399989, 210000, 209987, 202361]
        for j in range(5):
            table = HashTable(size[j], base)
            time_taken = time_inserting(content, table)
            #avg_probeLength = table.probe_length / table.count
            data = str(size[j]) + ', ' + str(time_taken) + '\n'#+ ', ' + str(table.collision) + ', ' + str(
                #table.track_avg_probe_length()) + '\n'
            write_file(data)'''