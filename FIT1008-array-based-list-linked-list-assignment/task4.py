'''
ID: 28390121
author: Priscilla Tham
Date: 28.04.2018
'''
from task2 import Array
from task3 import LinkedList as Array

def opening(filename):
    '''
    functions opens and reads a file
    precondition: file exist in directory
    :param filename: the file the user wants to open and read
    postcondition:
    :return: lines of the file
    complexity: best and worst: O(1)
    '''
    file = open(filename + '.txt')
    content = file.read()
    file.close()
    item = content.split('\n')
    return item

if __name__ == '__main__':
    filename = input('Enter filename: ')
    content = opening(filename)
    file_list = Array()
    for i in range(len(content)):
        file_list.append(content[i])
