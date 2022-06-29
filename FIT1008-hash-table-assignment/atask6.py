'''
ID: 28390121
author: Priscilla Tham
Date: 25.05.2018
'''
from atask2 import open_file
from atask4 import HashTableQuadratic


def ranking(table):
    maximum = 0
    for item in table:
        if item[1] > maximum:
            maximum = item[1]
    print(maximum)

    for item in table:
        if item[1] >= maximum / 100:
            table[item[0]] = 'common'
        elif item[1] >= maximum / 1000:
            table[item[0]] = 'uncommon'
        elif item[1] < maximum / 1000:
            table[item[0]] = 'rare'


def freq_count(content, table):
    punctuations = '''"`~!@#$%^&*()_+-={}[]|\:;<>?,./"'''
    stripped_content = ''

    for i in range(len(content)):
        string = ''
        for j in range(len(content[i])):
            if content[i][j] not in punctuations:
                string += content[i][j]

        words = string.split(' ')
        for k in range(len(words)):
            stripped_content += words[k].lower() + ' '

    stripped_content = stripped_content.split(' ')
    for m in range(len(stripped_content)):
        if stripped_content[m] not in table:
            table[stripped_content[m]] = 1
        else:
            count = table[stripped_content[m]]
            count += 1
            table[stripped_content[m]] = count


if __name__ == '__main__':
    filename = input('Enter file: ')
    content = open_file(filename)
    table = HashTableQuadratic(400000, 101)
    freq_count(content, table)
    ranking(table)
    print(table)
