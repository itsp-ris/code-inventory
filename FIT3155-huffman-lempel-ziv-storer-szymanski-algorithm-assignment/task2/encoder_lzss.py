'''
ID: 28390121
author: Priscilla Tham
Date: 07/06/2020
'''
import argparse as ap


def write_file(filename, output):
    with open(filename, 'w+b') as file:
        file.write(output)
    return


def getIndexAndLength(z_arr, pat_len, start):
    '''
    function gets the position of the starting character which matches pat_len characters the most and the number of
    matching characters
    precondition:
    :param z_arr: the array containing the length of the substring that matches the pat_len characters at each positions
           pat_len: the length of the characters to match against
           start: the starting position of the pat_len characters
    postcondition:
    :return: a) the position of the starting character which matches pat_len characters the most
             b) the number of matching characters
    complexity: time: best and worst: O(win_sz)
                space:
    error handling:
    '''
    mx = pat_len
    for i in range(pat_len + 1, len(z_arr)):
        if z_arr[i] > z_arr[mx]:
            mx = i
    return start + (mx - pat_len), z_arr[mx]


def countMatchingChar(pat, i, j):
    '''
    function counts the number of matches between pairs of characters
    precondition:
    :param pat: the string to pre-process
           i and j: indices to retrieve characters
    postcondition: the string is not modified
    :return: the number of matches
    complexity: time: best and worst: O(q) where q is the number of matching characters
                space:
    error handling:
    '''
    count = 0
    # when number of matching characters == 1, loop runs 1 time
    # when number of matching characters > 1 consecutively, loop runs q times
    while j < len(pat) and pat[j - i] == pat[j]:
        count += 1
        j += 1
    return count


def getZArr(pat):
    '''
    function fills up the z_arr array with the length of the substring that matches the prefix at each position of the
    string
    precondition:
    :param pat: the string to pre-process
    postcondition: the string is not modified
    :return: the z_arr array
    complexity: time: best and worst: O(win_sz + lookahead + q) where q is the number of
                             matching characters
                space: O(win_sz + lookahead)
    error handling:
    '''
    pat_len = len(pat)
    # when number of characters == 1, loop runs 1 time
    # when number of characters > 1, loop runs m times
    z_arr = [0 for _ in range(pat_len)]

    index = 0
    # when number of characters == 1, loop runs 1 time
    # when number of characters > 1, loop runs m - 1 times
    for i in range(1, pat_len):
        if 0 < z_arr[index] < i < z_arr[index] + index:
            count = z_arr[i - index]
            suffix_len = z_arr[index] + index - i
            if count == suffix_len:
                # when all characters is the same, loop does not run
                # when all characters is not the same, loop does not run
                # when substring matches the prefix exist, loop runs p times q, p * O(q)
                # where p is the number of substrings and q is the number of matching characters < m that is
                # retrieved by comparing pairs of characters rather than dynamic programming
                count += countMatchingChar(pat, i, z_arr[index] + index)
                z_arr[i] = count
            elif count < suffix_len:
                z_arr[i] = count
            elif count > suffix_len:
                z_arr[i] = suffix_len
        else:
            # when all characters is the same, loop runs once, 1 * O(m)
            # when all characters is not the same, loop runs m times once, m * O(1)
            # when substring matches the prefix exist, loop runs p times q, p * O(q)
            # where p is the number of substrings and q is the number of matching characters < m that is
            # retrieved by comparing pairs of characters rather than dynamic programming
            count = countMatchingChar(pat, i, i)
            z_arr[i] = count

        # updates to the biggest z-box
        if z_arr[i] > z_arr[index]:
            index = i
    z_arr[0] = pat_len
    return z_arr


def preprocess(txt, post, lookahead, win_sz):
    '''
    function concatenates the characters in the lookahead buffer with the characters in the window size
    precondition:
    :param: txt: the text string
            post: the current position in the text string
            lookahead: the lookahead buffer
            win_sz: the window size
    postcondition:
    :return: the string is not modified
    complexity: time: best and worst: O(win_sz + lookahead)
                space: O(win_sz + lookahead)
    error handling:
    '''
    string = ''
    limit = min(len(txt), post + lookahead)
    for j in range(post, limit):
        string += txt[j]

    limit = max(0, post - win_sz)
    for k in range(limit, limit + win_sz):
        string += txt[k]
    return string


def getEliasEncoding(n):
    '''
    function encodes the binary in Elias omega
    precondition:
    :param: n: the integer in binary
    postcondition:
    :return:
    complexity: time: best and worst: O(k) where p is the number of bits to represent the integer in binary
                space: O(k) where p is the number of bits to represent the integer in binary
    error handling:
    '''
    n = bytearray(n)
    n_len = len(n) - 1
    while n_len > 0:
        new = decToBin(n_len, [])
        new[0] = 0
        n = bytearray(new) + n
        n_len = len(new) - 1
    return n


def decToBin(n, res):
    '''
    function converts integers in decimal to binary
    precondition:
    :param: n: the integer in decimal
            res: the array to store the bits
    postcondition:
    :return:
    complexity: time: best and worst: O(log m) where m is the number of unique characters or the window size or the
                                      lookahead buffer
                space: O(k) where k is the number of bits to represent the integer in binary
    error handling:
    '''
    if n == 0:
        return res
    else:
        decToBin(n//2, res)
        res += [n % 2]
        return res


def rise(heap):
    '''
    function moves item up the heap accordingly
    precondition:
    :param: heap: the heap array
    postcondition: heap array is stable
    :return:
    complexity: time: best and worst: O(log unique)
                space:
    error handling:
    '''
    n = len(heap)-1
    # loop runs log k time(s)
    while n > 1 and (len(heap[n//2][0]) < len(heap[n][0]) or
                     (len(heap[n//2][0]) == len(heap[n][0]) and heap[n//2][1] > heap[n][1])):
        heap[n//2], heap[n] = heap[n], heap[n//2]
        n //= 2


def heapify(heap, index):
    '''
    function sorts items in the heap by sub-heap tree
    precondition:
    :param: heap: the heap array
    postcondition: heap array is stable
    :return:
    complexity: time: best and worst: O(log unique)
                space:
    error handling:
    '''
    root = 1
    heap_sz = len(heap)
    # loop runs log k time(s)
    while 2*root <= index:
        smallest = root
        left = 2*root
        right = 2*root+1

        if left < heap_sz and (len(heap[left][0]) > len(heap[smallest][0]) or
                    (len(heap[left][0]) == len(heap[smallest][0]) and
                     heap[left][1] < heap[smallest][1])):
            smallest = left

        if right < heap_sz and (len(heap[right][0]) > len(heap[smallest][0]) or
                    (len(heap[right][0]) == len(heap[smallest][0]) and
                     heap[right][1] < heap[smallest][1])):
            smallest = right

        if smallest == root:
            return
        heap[smallest], heap[root] = heap[root], heap[smallest]
        root = smallest


def heapSort(heap):
    '''
    function sorts items in the heap
    precondition:
    :param: heap: the heap array
    postcondition: heap array is stable
    :return:
    complexity: time: best and worst: O(unique log unique)
                space: O(unique)
    error handling:
    '''
    n = len(heap)-1
    # when number of items == 1, loop runs 1 time, loop in heapify runs 1 time
    # when number of items > 1, loop runs n times, loop in heapify function runs log k times
    for n in range(n, 0, -1):
        heap[1], heap[n] = heap[n], heap[1]
        heapify(heap, n)


def getHuffmanEncoding(heap, ascii):
    '''
    function encodes the unique characters in huffman
    precondition:
    :param heap: the heap array containing the unique characters
           ascii: the number of possible characters
    postcondition:
    :return: the array of possible characters with their huffman encoding if existed
    complexity: time: best and worst: O(unique log unique)
                space: O(ascii) where ascii = 256
    error handling:
    '''
    heapSort(heap)
    huffman = [bytearray() for _ in range(ascii)]
    while len(heap) > 2:
        item = heap[1]
        for i in range(len(item[0])):
            huffman[ord(item[0][i])].insert(0, 0)
        new_item = [item[0], item[1]]
        heap.remove(item)

        item = heap[1]
        for j in range(len(item[0])):
            huffman[ord(item[0][j])].insert(0, 1)
        new_item = [new_item[0] + item[0], new_item[1] + item[1]]
        heap.remove(item)
        heap += [new_item]
        rise(heap)
    return huffman


def getOccurence(pat, ascii):
    '''
    function counts the number of times each character in the string appears in the string
    precondition:
    :param pat: the string to pre-process
           ascii: the number of possible characters
    postcondition: the string is not modified
    :return: the array of possible characters which stores their count if they exist
    complexity: time: worst: O(n) where n is the number of characters in the pattern
                space: O(ascii) where ascii = 256
    error handling:
    '''
    char = [0 for _ in range(ascii)]
    # when number of characters == 1, loop runs 1 time
    # when number of characters > 1, loop runs m times
    for j in range(len(pat)):
        char[ord(pat[j])] += 1
    return char


def getUnique(pat, ascii):
    '''
    function counts the unique characters
    precondition:
    :param pat: the string to pre-process
    postcondition: the string is not modified
    :return: a) the number of unique characters and
             b) the heap containing the unique characters and its frequency
    complexity: time: worst: O(n) where n is the number of characters in the text
                space: O(ascii) where ascii = 256
    error handling:
    '''
    # O(m)
    char = getOccurence(pat, ascii)
    unique = 0
    heap = [None]
    # loop runs constant time
    # counts unique characters
    for i in range(ascii):
        if char[i] > 0:
            unique += 1
            heap += [[chr(i), char[i]]]
    return unique, heap


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
        file = open(filename, 'r')
        for line in file:
            string += line
        file.close()
        return string
    except FileNotFoundError:
        return string


def encoder_lzss(txtfile, win_sz, lookahead):
    '''
    function encodes the file content in Lempel-Ziv-Storer-Szymanski (LZSS)
    precondition:
    :param txtfile: the filename containing the text to encode
           windowfile: the filename containing the window size
           lookaheadfile: the filename containing the lookahead buffer
    postcondition: the string is not modified
    :return:
    complexity: time: best and worst: O(n*win_sz + n*lookahead + n*q) where n is the number of characters in the
                                      text and q is the number of matching characters
                space: O(kn) where k is the number of bits to represent the characters in binary and n is the number of
                characters in the text
    error handling:
    '''
    ascii = 256
    txt = open_file(txtfile)
    txt_len = len(txt)

    # O(n)
    unique, heap = getUnique(txt, ascii)
    # O(unique log unique)
    huffman = getHuffmanEncoding(heap, ascii)
    # O(k log unique)
    header = getEliasEncoding(decToBin(unique, []))
    for k in range(ascii):
        if len(huffman[k]) > 0:
            # O(log 7) + O(k log unique)
            header += bytearray(decToBin(k, [])) + getEliasEncoding(decToBin(len(huffman[k]), [])) + huffman[k]

    data = bytearray([1]) + huffman[ord(txt[0])]
    m = 1
    count = 1
    # O(n)
    while m < len(txt):
        # O(win_sz + lookahead)
        preprocessed = preprocess(txt, m, lookahead, win_sz)
        pat_len = min(txt_len - m, lookahead)
        start = max(0, m - win_sz)
        # O(win_sz + lookahead + q)
        z_arr = getZArr(preprocessed)
        # O(lookahead)
        index, length = getIndexAndLength(z_arr, pat_len, start)
        if length >= 3 and m > index:
            limit = min(lookahead, length)
            # O(k log win_sz) + O(k log lookahead)
            data += bytearray([0]) + getEliasEncoding(decToBin(m - index, [])) + getEliasEncoding(decToBin(limit, []))
            m += limit
            count += 1
        else:
            data += bytearray([1]) + huffman[ord(txt[m])]
            m += 1
            count += 1
    # O(k log n)
    data = getEliasEncoding(decToBin(count, [])) + data
    extension = bytearray([0 * len(header + data) % 8])
    output = header + data + extension
    write_file('output_encoder_lzss.bin', output)
    return


def main():
    # create a parser object
    parser = ap.ArgumentParser()

    # specify what arguments will be coming from the terminal/commandline
    parser.add_argument("txtfile", help="specifies an ASCII text file", type=str)
    parser.add_argument("W", help="specifies search window size", type=int)
    parser.add_argument("L", help="specifies lookahead buffer size", type=int)

    # get all the arguments
    arguments = parser.parse_args()

    # Extract the required arguments
    txtfile = arguments.txtfile
    W = arguments.W
    L = arguments.L

    encoder_lzss(txtfile, W, L)


if __name__ == '__main__':
    main()
