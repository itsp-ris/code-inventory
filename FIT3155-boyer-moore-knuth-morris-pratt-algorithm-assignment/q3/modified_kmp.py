'''
ID: 28390121
author: Priscilla Tham
Date: 10.04.2020
'''
from mirrored_boyermoore import writeFile
from mirrored_boyermoore import openFile
from mirrored_boyermoore import getZArr
from mirrored_boyermoore import getUniqueAndIndex
import argparse as ap


def spxRule(txt, spx_arr, char, i, j):
    '''
    functions calculates the shift if the matching substring proper suffix exist in the pattern prefix
    precondition:
    :param txt: the string required to retrieve matching substring
           spx_arr: the array storing the shift to the pattern prefix which matches with the pattern proper suffix
           char: the array of possible characters which stores their position instead of their count if they exist
           i and j: indices to shift
    postcondition:
    :return: the i and j indices after shifting
    complexity: time: worst: O(n) where n = 1
                space:
    error handling:
    '''
    pat_len = len(spx_arr[0])
    if char[ord(txt[i + j]) - 32] > 0:
        shift = (j - 1) - spx_arr[char[ord(txt[i + j]) - 32] - 1][j - 1]
    else:
        shift = 1

    if shift != pat_len and shift != 1:
        # Galil's optimization; skip sure matched characters
        j = spx_arr[char[ord(txt[i + j]) - 32] - 1][j - 1] + 1
    else:
        j = 0
    i += shift
    return i, j


def getSpxArr(pat):
    '''
    functions fills up the spx_arr array with the shift to the string prefix which matches with the string proper suffix
    precondition:
    :param pat: the string to pre-process
    postcondition:
    :return: the spx_arr array
    complexity: time: worst: O(km) where k is the total unique characters and m is the length of the pattern
                             string
                space: O(km) where k is the total unique characters and m is the length of the pattern string
    error handling:
    '''
    zArr = getZArr(pat)
    print(zArr)
    unique, char = getUniqueAndIndex(pat)

    pat_len = len(pat)
    mx = zArr[1]
    # when number of characters == 1, loop runs 1 time
    # when number of characters > 1, loop runs m times
    for j in range(2, pat_len):
        mx = max(mx, zArr[2])

    # when length of the pattern string == 1, inner loop runs 1 time
    # when length of the pattern string > 1, inner loop runs m times
    # when number of unique characters == 1, outer loop runs 1 time
    # when number of unique character > 1, outer loop runs k times
    spx_arr = [[-2 for _ in range(pat_len)] for _ in range(unique - 1)]
    # when length of the pattern string == 1, loop runs 1 time
    # when length of the pattern string > 1, loop runs m - 1 times
    for i in range(pat_len - 1, 0, -1):
        if zArr[i] > 0:
            j = i + zArr[i] - 1
            spx_arr[char[ord(pat[i]) - 32] - 1][j] = zArr[i] - 1
    return mx, spx_arr, char


def modified_kmp(txtfile, patfile):
    '''
    functions finds pattern in text using the Knuth-Morris-Pratt algorithm with the addition of shifting to match the
    unmatched character
    precondition: content of the text file consists of printable ascii only
    :param txtfile: the filename which contains the text string
           patfile: the filename which contains the pattern string
    postcondition: content of the file is not modified
    :return:
    complexity: time: worst: O(n + m) where n is the number of characters in the text string and m is the
                             number of characters in the pattern
                space: O(km) where k is the total unique characters and m is the length of the pattern string
    error handling:
    '''
    txt = openFile(txtfile)
    pat = openFile(patfile)

    # O(km)
    mx, spx_arr, char = getSpxArr(pat)
    pat_len = len(pat)

    i = 0
    j = 0
    output = []
    # when number of characters == 1, loop runs 1 time
    # when number of characters > 1, loop runs n time
    while (i + j) < len(txt):
        if txt[i + j] != pat[j]:
            i, j = spxRule(txt, spx_arr, char, i, j)
        else:
            j += 1

            if j >= pat_len:
                output += [i + 1]
                # go to the next unchecked character to find subsequent matching pattern in text
                i = i + (pat_len - mx)
                j = mx
    writeFile('output_kmp.txt', output)
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

    modified_kmp(txtfile, patfile)


if __name__ == '__main__':
    # main()
    modified_kmp('txtfile.txt', 'patfile.txt')