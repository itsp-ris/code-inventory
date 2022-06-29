'''
ID: 28390121
author: Priscilla Tham
Date: 10/05/2020
'''
from wildcard_suffixtree_matching import get_tree
from wildcard_suffixtree_matching import open_file
import argparse as ap


def write_file(filename, string):
    '''
    function writes to file
    precondition:
    :param  filename: the name of the new file
            output: the content to write to the file
    postcondition:
    :return:
    complexity: time: best and worst: O(k) where k is the number of characters in the text
                space:
    error handling:
    '''
    with open(filename, 'w') as file:
        file.write(string)
    return


def get_bwt(txt, suffix_arr):
    '''
    function computes the burrows-wheeler's transform from the suffix array of a text
    precondition:
    :param: suffix_arr: the suffix array of a text
    postcondition:
    :return:
    complexity: time: best and worst: O(k) where k is the number of characters in the text
                space: O(k) where k is the number of characters in the text
    error handling:
    '''
    txt_length = len(txt)
    bwt = ''
    # when number of characters == 1, loop runs 1 time
    # when number of characters > 1, loop runs k times
    for i in range(txt_length):
        bwt += txt[(suffix_arr[i] - 1 + txt_length) % txt_length]
    return bwt


def dfs(node, txt, count, suffix_arr):
    '''
    function computes the suffix array of a text from the tree
    precondition:
    :param: node: the current position in the tree which represents the current substring in the text
            txt: the text string
            count: the current length of a substring
            suffix_arr: the array to be appended of positions in the text string where the substring exists
    postcondition:
    :return:
    complexity: time: best and worst: O(n) where n is the number of nodes
                space: O(k) where k is the number of characters in the text
    error handling:
    '''
    printables = 95
    txt_length = len(txt)
    i = 0
    # when all characters in text string is different, loop runs n times
    # otherwise, loop runs 2n times
    while len(suffix_arr) < txt_length:
        # find a child node in lexicographical order
        if node.child[i]:
            substring_length = node.child[i].end - node.child[i].start + 1
            count += substring_length
            if node.child[i].end < txt_length - 1:
                # move to the child node if not the end of substring
                dfs(node.child[i], txt, count, suffix_arr)
            else:
                suffix_arr += [txt_length - count]
            count -= substring_length
        i += 1
        if not i < printables:
            return
    return suffix_arr


def suffixtree2bwt(txtfile):
    '''
    function uses the suffix tree to obtain the burrows-wheeler's transform of text
    precondition:
    :param: txtfile: the name of the file containing the text sting
    postcondition: the content of the file is not modified
    :return:
    complexity: time: best and worst: O(n) where n is the number nodes
                space: O(n) where n is the number of nodes
    error handling:
    '''
    txt = open_file(txtfile) + '$'
    # O(n)
    tree = get_tree(txt, 32)
    # O(n)
    suffix_arr = dfs(tree.head, txt, 0, [])
    # O(k)
    bwt = get_bwt(txt, suffix_arr)
    write_file('output_bwt.txt', bwt)
    return


def main():
    # create a parser object
    parser = ap.ArgumentParser()

    # specify what arguments will be coming from the terminal/commandline
    parser.add_argument("txtfile", help="specifies the name of the text file containing str[1...n]", type=str)

    # get all the arguments
    arguments = parser.parse_args()

    # Extract the required arguments
    txtfile = arguments.txtfile

    suffixtree2bwt(txtfile)


if __name__ == '__main__':
    # main()
    suffixtree2bwt('test.txt')