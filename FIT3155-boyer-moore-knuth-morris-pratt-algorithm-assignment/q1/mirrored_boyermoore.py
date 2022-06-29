'''
ID: 28390121
author: Priscilla Tham
Date: 10.04.2020
'''
import argparse as ap


def writeFile(filename, output):
    '''
    function writes to file
    precondition:
    :param output: the content to write to the file
    postcondition:
    :return:
    complexity: time: worst: O(r) where r is the length of output
                space:
    error handling:
    '''
    string = ''
    for i in range(len(output)):
        string += str(output[i]) + '\n'
    with open(filename, 'w', encoding='utf-8-sig') as file:
        file.write(string)
    return


def matchedSuffixRule(matched_suffix, i, j, pat_len):
    '''
    function calculates the shift if the matched prefix exist in the pattern suffix to align
    precondition:
    :param matched_suffix: the array storing maximum length of the prefix that contains in or matches the
           suffix at each position of the pattern string
           i and j: indices to shift
           pat_len: length of the pattern string
    postcondition: all parameters except indices is not modified
    :return: the i and j indices after shifting
    complexity: time: worst: O(n) where n = 1
                space:
    error handling:
    '''
    i = i - (pat_len - matched_suffix[j])
    j = 0
    return i, j


def goodPrefixRule(good_prefix, i, j):
    '''
    function calculates the shift if the matched substring exist to the right of the pattern to align
    precondition:
    :param good_prefix: the array storing next nearest occurrence to the right of each substring in the pattern
           i and j: indices to shift
    postcondition: all parameters except indices is not modified
    :return: the i and j indices after shifting
    complexity: time: worst: O(n) where n = 1
                space:
    error handling:
    '''
    i -= good_prefix[j]
    j = 0
    return i, j


def badCharRule(txt, right_leftmost, char, i, j):
    '''
    function calculates the shift if the unmatched character exist to the right of the pattern to align
    precondition:
    :param txt: the string required to retrieve unmatched characters, matching substring and matching suffix
           right_leftmost: the matrix table storing next nearest occurrence to the right of each character in the
           pattern
           char: the array of possible characters which stores their position instead of their count if they exist
           i and j: indices to shift
    postcondition: all parameters except indices is not modified
    :return: the i and j indices after shifting
    complexity: time: worst: O(n) where n = 1
                space:
    error handling:
    '''
    i -= abs(j - right_leftmost[char[ord(txt[i + j]) - 32] - 1][j])
    j = 0
    return i, j


def allMatchedRule(matched_suffix, i, pat_len):
    '''
    function calculates the shift if the whole pattern exist in the text
    precondition:
    :param matched_suffix: the array storing maximum length of the prefix that contains in or matches the
           suffix at each position of the pattern string
           i: index to shift
           pat_len: length of the pattern string
    postcondition: all parameters except index is not modified
    :return: the i and j indices after shifting
    complexity: time: worst: O(n) where n = 1
                space:
    error handling:
    '''
    i = i - (pat_len - matched_suffix[1])
    j = 0
    return i, j


def computeShift(txt, right_leftmost, char, z_arr, good_prefix, matched_suffix, i, j, pat_len):
    '''
    function determines the best shift
    precondition:
    :param txt: the string required to retrieve unmatched characters, matching substring and matching suffix
           right_leftmost: the matrix table storing next nearest occurrence to the right of each character in the
           pattern
           char: the array of possible characters which stores their position instead of their count if they exist
           good_prefix: the array storing next nearest occurrence to the right of each substring in the pattern
           matched_suffix: the array storing maximum length of the prefix that contains in or matches the
           suffix at each position of the pattern string
           i and j: indices to shift
           pat_len: length of the pattern string
    postcondition: all parameters except indices is not modified
    :return: the i and j indices after shifting
    complexity: time: worst: O(n) where n = 1
                space:
    error handling:
    '''
    previous = [i, j]
    if char[ord(txt[i + j]) - 32] > 0:
        if good_prefix[j] >= right_leftmost[char[ord(txt[i + j]) - 32] - 1][j] > 0:
            i, j = goodPrefixRule(good_prefix, i, j)
            if previous[0] - i > 1: previous[1] = z_arr[good_prefix[previous[1]]]
            if previous[0] - i == pat_len: previous[1] = 0

        elif right_leftmost[char[ord(txt[i + j]) - 32] - 1][j] > 0:
            i, j = badCharRule(txt, right_leftmost, char, i, j)
            previous[1] = 1
        else:
            i, j = matchedSuffixRule(matched_suffix, i, j, pat_len)
            if previous[0] - i > 1: previous[1] = matched_suffix[previous[1]]
    else:
        if good_prefix[j] > 0:
            i, j = goodPrefixRule(good_prefix, i, j)
            if previous[0] - i > 1: previous[1] = z_arr[good_prefix[previous[1]]] - 1
            if previous[0] - i == pat_len: previous[1] = 0
        else:
            i, j = matchedSuffixRule(matched_suffix, i, j, pat_len)
            if previous[0] - i > 1: previous[1] = matched_suffix[previous[1]]
    return i, j, previous


def countMatchingChar(pat, i, j):
    '''
    function counts the number of matches between pairs of characters
    precondition:
    :param pat: the string to pre-process
           i and j: indices to retrieve characters
    postcondition: the string is not modified
    :return: the number of matches
    complexity: time: worst: O(q) where q is the number of matching characters
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
    complexity: time: worst: O(m + q) where m is the number of characters in the pattern and q is the number of
                             matching characters
                space: O(m) where m is the number of characters in the pattern
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


def getMatchedSuffix(pat, z_arr):
    '''
    function fills up the matched_suffix array with the maximum length of the prefix that contains in or matches the
    suffix at each position of the string
    precondition:
    :param pat: the string to pre-process
    postcondition: the string is not modified
    :return: the matched_suffix array
    complexity: time: worst: O(m) where m is the number of characters in the pattern
                space: O(m) where m is the number of characters in the pattern
    error handling:
    '''
    # O(m + q)
    matched_suffix = z_arr
    mx = matched_suffix[-1]
    # when number of characters == 1, loop runs 1 time
    # when number of characters > 1, loop runs m - 2 times
    for i in range(len(pat) - 2, 0, -1):
        mx = max(mx, matched_suffix[i])
        matched_suffix[i] = mx
    return matched_suffix


def getGoodPrefix(pat, z_arr):
    '''
    function fills up the good_prefix array with the next nearest occurrence to the right of each substring in the
    string
    precondition:
    :param pat: the string to pre-process
    postcondition: the string is not modified
    :return: the good_prefix array
    complexity: time: worst: O(m) where m is the number of characters in the pattern
                space: O(m + 1) where m is the number of characters in the pattern
    error handling:
    '''
    pat_len = len(pat)
    # when number of characters == 1, loop runs 1 time
    # when number of characters > 1, loop runs m + 1 times
    good_prefix = [0 for _ in range(pat_len + 1)]
    # when number of characters == 1, loop runs 1 time
    # when number of characters > 1, loop runs m times
    for i in range(pat_len - 1, 0, -1):
        j = (pat_len + z_arr[i]) % pat_len
        good_prefix[j] = i
    return good_prefix


def getRightLeftmost(pat, unique, char):
    '''
    function fills up the right_leftmost matrix table with its next nearest occurrence to the right of each
    character in the string
    precondition:
    :param pat: the string to pre-process
           unique: total unique characters + 1
           char: the array of possible characters which stores their position instead of their count if they exist
    postcondition: the string is not modified
    :return: the matrix table
    complexity: time: worst: O(km) where k is the total unique characters and m is the length of the pattern
                             string
                space: O(km) where k is the total unique characters and m is the length of the pattern string
    error handling:
    '''
    pat_len = len(pat)
    # when length of the pattern string == 1, inner loop runs 1 time
    # when length of the pattern string > 1, inner loop runs m times
    # when number of unique characters == 1, outer loop runs 1 time
    # when number of unique character > 1, outer loop runs k times
    # initialised with value = length of pattern
    # cannot initialise with value = 0 because index starts from 0 and right_leftmost stores them
    right_leftmost = [[pat_len for _ in range(pat_len)] for _ in range(unique - 1)]
    # when length of the pattern string == 1, loop runs 1 time
    # when length of the pattern string > 1, loop runs m times
    for i in range(pat_len):
        right_leftmost[char[ord(pat[i]) - 32] - 1][i] = i

    # when number of unique characters == 1, loop runs 1 time
    # when number of unique character > 1, loop runs k times
    for j in range(unique - 1):
        # when length of the pattern string == 1, loop runs 1 time
        # when length of the pattern string > 1, loop runs m - 1 times
        for k in range(pat_len - 2, -1, -1):
            # update all positions to the left of right_leftmost[j][k + 1] if empty (value == length of pattern)
            # with value stored at right_leftmost[j][k + 1]
            if right_leftmost[j][k] == pat_len:
                right_leftmost[j][k] = right_leftmost[j][k + 1]
    return right_leftmost


def getOccurence(pat, ascii):
    '''
    function counts the number of times each character in the string appears in the string
    precondition:
    :param pat: the string to pre-process
           ascii: the number of possible characters
    postcondition: the string is not modified
    :return: the array of possible characters which stores their count if they exist
    complexity: time: worst: O(m) where m is the number of characters in the pattern
                space: O(ascii) where ascii = 95
    error handling:
    '''
    char = [0 for _ in range(ascii)]
    # when number of characters == 1, loop runs 1 time
    # when number of characters > 1, loop runs m times
    for i in range(len(pat)):
        index = ord(pat[i]) - 32
        # do not increase count of '$'
        if index != 4:
            char[index] += 1
    return char


def getUniqueAndIndex(pat):
    '''
    function counts the unique characters and set their position in the right_leftmost matrix table
    precondition:
    :param pat: the string to pre-process
    postcondition: the string is not modified
    :return: a) the number of unique characters and
             b) the array of possible characters which stores their position instead of their count if they exist
    complexity: time: worst: O(m) where m is the number of characters in the pattern
                space: O(ascii) where ascii = 95
    error handling:
    '''
    ascii = 95
    # O(m)
    char = getOccurence(pat, ascii)
    unique = 1
    # loop runs constant time
    # counts unique characters
    for i in range(ascii):
        if char[i] > 0:
            # stores position of the characters in the right_leftmost matrix table using unique
            # position starts from 1 (unique = 1 initially)
            # therefore, unique = total unique characters + 1
            char[i] = unique
            unique += 1
    return unique, char


def openFile(filename):
    '''
    function opens file
    precondition: content of the file consists of printable ascii only
    :param filename: the file to open
    postcondition: content of the file is not modified
    :return: content of the file
    complexity: time: worst: O(n) where n = 1
                space:
    error handling: return string of length 0
    '''
    try:
        with open(filename, 'r', encoding='utf-8-sig') as file:
            content = file.read()
    except FileNotFoundError:
        content = ''
    return content


def mirrored_boyermoore(txtfile, patfile):
    '''
    function finds pattern in text using the boyer moore algorithm in reverse
    precondition: content of the file consists of printable ascii only
    :param txtfile: the filename which contains the text string
           patfile: the filename which contains the pattern string
    postcondition: content of the file is not modified
    :return:
    complexity: time: worst: O(n + m) where n is the number of characters in the text string and m is the
                             number of characters in the pattern
                space: O(km) where k is the total unique characters and m is the length of the pattern string
    error handling:
    '''
    txt = txtfile
    pat = patfile

    unique, char = getUniqueAndIndex(pat)

    # bad character matrix table
    # O(km)
    right_leftmost = getRightLeftmost(pat, unique, char)
    z_arr = getZArr(pat)
    # good prefix array
    # O(m + q)
    good_prefix = getGoodPrefix(pat, z_arr)
    # matched suffix array
    # O(m + q)
    matched_suffix = getMatchedSuffix(pat, z_arr)

    txt_len = len(txt)
    pat_len = len(pat)

    i = txt_len - pat_len
    j = 0
    previous = [len(txt), len(txt)]
    output = []
    # when number of characters == 1, loop runs 1 time
    # when number of characters > 1, loop runs n times
    while i >= 0:
        if txt[i + j] != pat[j]:
            i, j, previous = computeShift(txt, right_leftmost, char, z_arr, good_prefix, matched_suffix, i, j, pat_len)
        else:
            # Galil's optimization; skip sure matched characters
            if (i + j) == previous[0]:
                j = j + previous[1]

            j += 1

            if j >= pat_len:
                output += [i + 1]
                # go to the next unchecked character to find subsequent matching pattern in text
                i, j = allMatchedRule(matched_suffix, i, pat_len)
    out = [n for n in range(len(txt)) if txt.find(pat, n) == n]
    print(len(output), len(out), pat)
    # writeFile('output_mirrored_boyermoore.txt', output[::-1])
    return


def main():
    # create a parser object
    parser = ap.ArgumentParser()

    # specify what arguments will be coming from the terminal/commandline
    parser.add_argument("txtfile", help="specifies the name of the text file", type=str)
    parser.add_argument("patfile", help="specifies the name of the pattern file", type=str)

    # get all the arguments
    arguments = parser.parse_args()

    # Extract the required arguments
    txtfile = arguments.txtfile
    patfile = arguments.patfile

    mirrored_boyermoore(txtfile, patfile)


if __name__ == '__main__':
    # main()
    txt = openFile('reference.txt')
    pat = openFile('pattern.txt').split()
    mirrored_boyermoore(txt, pat[1])

