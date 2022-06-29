'''
ID: 28390121
author: Priscilla Tham
Date: 10/05/2020
'''
from wildcard_suffixtree_matching import get_tree
from wildcard_suffixtree_matching import open_file
import argparse as ap


def write_file(filename, pairs, lcp_arr):
    '''
    function writes to file
    precondition:
    :param  filename: the name of the new file
            output: the content to write to the file
    postcondition:
    :return:
    complexity: time: best and worst: O(r) where r is the number of pairs
                space:
    error handling:
    '''
    string = ''
    i = 1
    j = i - 1
    # when number of elements == 1, loop runs 1 time
    # when number of elements > 1, loop runs r times
    while i < len(pairs):
        string += str(pairs[i - 1] + 1) + ' ' + str(pairs[i] + 1) + ' ' + str(lcp_arr[j]) + '\n'
        i += 2
        j += 1
    with open(filename, 'w') as file:
        file.write(string)
    return


def lcps(txtfile, pairsfile):
    '''
    function computes the longest common prefix between two suffixes using the suffix tree
    precondition:
    :param  txtfile: the name of the file containing the text string
            pairsfile: the name of the file containing the pairs of suffixes
    postcondition: the content of the files are not modified
    :return:
    complexity: time: best and worst: O(nr) where n is the number of nodes and r is the number of pairs
                space: O(n) where n is the number of nodes
    error handling:
    '''
    offset = 32
    txt = open_file(txtfile) + '$'
    txt_length = len(txt)

    pairs = open_file(pairsfile).split()
    # when number of elements == 1, loop runs 1 time
    # when number of elements > 1, loop runs 2r times
    for i in range(len(pairs)):
        pairs[i] = int(pairs[i]) - 1

    # O(n)
    tree = get_tree(txt, offset)
    tree.node = tree.head
    lcp_arr = []
    j = 1
    count = 0
    # when number of pairs == 1, loop runs 2n times
    # when number of pairs > 1, loop runs 2nr times
    while j < len(pairs):
        if count < txt_length - pairs[j] and count < txt_length - pairs[j - 1] and \
                txt[pairs[j] + count] == txt[pairs[j - 1] + count]:
            node = tree.node.child[ord(txt[pairs[j - 1] + count]) - offset]
            count += node.end - node.start + 1
            tree.node = node
        else:
            lcp_arr += [count]
            tree.node = tree.head
            count = 0
            j += 2
    write_file('output_lcps.txt', pairs, lcp_arr)
    return


def main():
    # create a parser object
    parser = ap.ArgumentParser()

    # specify what arguments will be coming from the terminal/commandline
    parser.add_argument("txtfile", help="specifies the name of the text file", type=str)
    parser.add_argument("pairsfile", help="specifies the name of the pairs file", type=str)

    # get all the arguments
    arguments = parser.parse_args()

    # Extract the required arguments
    txtfile = arguments.txtfile
    pairsfile = arguments.pairsfile

    lcps(txtfile, pairsfile)


if __name__ == '__main__':
    main()