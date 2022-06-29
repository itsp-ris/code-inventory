'''
ID: 28390121
author: Priscilla Tham
Date: 07/06/2020
'''
import argparse as ap


class TrieNode:

    def __init__(self, size=2):
        self.array = []
        # time and space complexity is constant
        self.child = [None]*size


class Trie:

    def __init__(self, size=2):
        # always points to the root/head
        self.head = TrieNode(size)
        # points to the current position
        self.node = self.head

    def append(self, data):
        '''
        function appends the item to the array of the node
        precondition:
        :param: data: item to be appended
        postcondition:
        :return:
        complexity: time: best and worst: O(p) where p = 1 is possible
                    space:
        error handling:
        '''
        node = self.node
        node.array += [data]

    def insert(self, char):
        '''
        function 'inserts' the item to the child node of the parent node
        precondition:
        :param: char: the item to be inserted
        postcondition: item is not stored inside the trie
        :return:
        complexity: time: best and worst: O(p) where p = 1 is possible
                    space: O(p) where p = 1 is possible as the creation of nodes is of constant size
        error handling:
        '''
        node = self.node
        index = int(char)
        if not node.child[index]:
            # runs in constant time
            node.child[index] = TrieNode()
        self.node = node.child[index]

    def search(self, key):
        '''
        function searches through tree for the item
        precondition:
        :param: key: item to be searched
        postcondition:
        :return: the array of the last node associated to the last character in the key
        complexity: time: best and worst: O(m) where m is the maximum number of characters of the key
                    space:
        error handling:
        '''
        node = self.head
        # when number of characters == 1, loop runs 1 time
        # when number of characters > 1, loop runs m times
        for i in range(len(key)):
            if not node.child[int(key[i])]:
                return []
            node = node.child[int(key[i])]
        return node.array


def write_file(filename, output):
    '''
    function writes to file
    precondition:
    :param  filename: the name of the new file
            output: the content to write to the file
    postcondition:
    :return:
    complexity: time: best and worst: O(p) where p is the length of output
                space:
    error handling:
    '''
    with open(filename, 'w') as file:
        file.write(output)
    return


def binToDec(string):
    '''
    function converts integers in binary to decimal
    precondition:
    :param: string: the bit string
    postcondition:
    :return:
    complexity: time: best and worst: O(k) where k is the number of bits to represent the integer in binary
                space: O(k) where k is the number of bits to represent the integer in binary
    error handling:
    '''
    return int(string, 2)


def getHuffmanTree(encoded, unique, start):
    '''
    function builds the trie to find the alphabet represented by its huffman encoding
    precondition:
    :param encoded: the encoded string
           unique: the number of unique characters
           start: the starting position in the encoded string containing the details of the alphabet
    postcondition:
    :return: the trie
    complexity: time: best and worst: O(k*unique) where k is the number of bits of all alphabets in huffman encoding
                space: O(k*unique) where k is the number of bits of all alphabets in huffman encoding
    error handling:
    '''
    trie = Trie()
    bits = 7
    char = None
    length = 0
    string = ''
    for i in range(start, len(encoded)):
        if unique == 0:
            trie.node = trie.head
            return trie, i
        if char and length != 0:
            trie.insert(encoded[i])
            length -= 1
            if length == 0:
                trie.append(chr(char))
                trie.node = trie.head
                unique -= 1
                bits = 7
                char = None
        else:
            string += encoded[i]
            bits -= 1
            if char and bits == 0 and string[0] == '0':
                string = string.replace(string[0], '1', 1)
                bits = binToDec(string) + 1
                string = ''
            elif char and bits == 0 and string[0] == '1':
                length = binToDec(string)
                string = ''
            elif bits == 0:
                char = binToDec(string)
                bits = 1
                string = ''


def getUnits(encoded, start=1):
    '''
    function retrieves the integer in binary from the encoded string and converts them to decimal
    precondition:
    :param encoded: the encoded string
           start: the starting position in the encoded string of the integer in binary
    postcondition:
    :return: the integer in binary
    complexity: time: best and worst: O(k) where k is the number of bits to represent the integer in binary
                space: O(k) where k is the number of bits to represent the integer in binary
    error handling:
    '''
    count = 2
    string = ''
    for i in range(start, len(encoded)):
        string += encoded[i]
        count -= 1
        if count == 0:
            if string[0] == '0':
                string = string.replace(string[0], '1', 1)
                count = binToDec(string) + 1
                string = ''
            else:
                units = binToDec(string)
                return units, i + 1


def open_file(filename):
    '''
    function opens a file
    precondition:
    :param  filename: the name of the file to open
    postcondition: the content of the file is not modified
    :return: the content of the file
    complexity: time: best and worst: O(n) where n is the number of characters in the file
                space: O(n) where n is the number of characters in the file
    error handling: return empty string when file does not exist
    '''
    string = ''
    try:
        file = open(filename, 'rb')
        binary = list(file.read())
        file.close()

        for i in range(len(binary)):
            string += str(binary[i])
        return string
    except FileNotFoundError:
        return string


def decoder_lzss(binfile):
    '''
    function decodes the Lempel-Ziv-Storer-Szymanski (LZSS) encoded string
    precondition:
    :param binfile: the file containing the encoded string
    postcondition:
    :return:
    complexity: time: best and worst: O(n*lookahead) where n is the number of characters in the encoded string
                space: O(n) where n is the number of characters in the encoded string
    error handling:
    '''
    encoded = open_file(binfile)
    unique, start = getUnits(encoded)
    huffman_tree, start = getHuffmanTree(encoded, unique, start)
    enc_units, start = getUnits(encoded, start + 1)

    i = start
    bits = 1
    code = None
    index = None
    string = ''
    decoded = ''
    # O(n)
    while len(encoded) > i and enc_units > 0:
        if code:
            string += encoded[i]
            bits -= 1
            if code == '0' and index and bits == 0 and string[0] == '1':
                n = len(decoded)
                l = binToDec(string)
                # O(lookahead)
                for j in range(n - index, n - index + l):
                    decoded += decoded[j]
                enc_units -= 1
                code = None
                index = None
                bits = 1
                string = ''
            elif code == '0' and bits == 0 and string[0] == '0':
                string = string.replace(string[0], '1', 1)
                bits = binToDec(string) + 1
                string = ''
            elif code == '0' and bits == 0 and string[0] == '1':
                index = binToDec(string)
                bits = 1
                string = ''
            elif code == '1':
                try:
                    # O(k)
                    decoded += huffman_tree.search(string)[0]
                    enc_units -= 1
                    code = None
                    bits = 1
                    string = ''
                except Exception:
                    pass
        else:
            code = encoded[i]
        i += 1
    write_file('output_decoder_lzss.txt', decoded)
    return


def main():
    # create a parser object
    parser = ap.ArgumentParser()

    # specify what arguments will be coming from the terminal/commandline
    parser.add_argument("binfile", help="specifies a binary file", type=str)

    # get all the arguments
    arguments = parser.parse_args()

    # Extract the required arguments
    binfile = arguments.binfile

    decoder_lzss(binfile)


if __name__ == '__main__':
    main()