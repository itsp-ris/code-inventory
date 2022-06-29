'''
ID: 28390121
author: Priscilla Tham
Date: 13.04.2020
'''
from mirrored_boyermoore import writeFile
from mirrored_boyermoore import openFile
from mirrored_boyermoore import getZArr
import argparse as ap


def getSegmentedZArr(segmented_pats, txt):
    '''
    function performs z algorithm on each segment$text string
    precondition:
    :param segmented_pats: segmented pattern which exclude wildcards
           txt: the string to concatenate with segmented pattern for pre-processing
    postcondition:
    :return: the z_arr array for each pattern segment
    complexity: time: worst: O(k(n + x) + q) where k is the number of pattern segments and n is the number of
                             characters in the text and x is a fraction of the characters in the pattern and
                             q is the number of matching characters
                space: O(k(n + x)) where k is the number of pattern segments and n is the number of characters in the
                       text and x is a fraction of the characters in the pattern
    error handling:
    '''
    segments = len(segmented_pats)
    segmented_z_arr = []
    for i in range(segments):
        # O((n + x) + q)
        # where n is the number of characters in the text
        # and x is a fraction of the characters in the pattern < m
        # and q is the number of matching characters < (n + x) that is retrieved by comparing pairs of characters
        # rather than dynamic programming
        z_arr = getZArr(segmented_pats[i] + '$' + txt)
        segmented_z_arr += [z_arr]
    return segmented_z_arr


def segment(pat):
    '''
    function segments the string to exclude wildcards
    precondition:
    :param pat: the string to pre-process
    postcondition:
    :return: the array of segmented patterns
    complexity: time: worst: O(m) where m is the number of characters in the pattern
                space: O(m) where m is the number of characters in the pattern
    error handling:
    '''
    pat_len = len(pat)
    segmented_pats = []
    consecutive_wildcards = [0 for _ in range(pat_len)]
    string = ''
    count = 0
    # when number of characters == 1, loop runs 1 time
    # when number of characters > 1, loop runs m times
    for i in range(pat_len - 1, -1, -1):
        if pat[i] != '?':
            string = pat[i] + string
            count = 0
        else:
            count += 1
            # store the number of consecutive wildcards from position i
            consecutive_wildcards[i] = count

        if (count == 1 or i == 0) and len(string) > 0:
            segmented_pats = [string] + segmented_pats
            string = ''
    return segmented_pats, consecutive_wildcards


def wildcard_matching(txtfile, patfile):
    '''
    function finds pattern in text using z algorithm
    precondition: content of the file consists of printable ascii only
    :param txtfile: the filename which contains the text string
           patfile: the filename which contains the pattern string
    postcondition: content of the file is not modified
    :return:
    complexity: time: worst: O(n + m) where n is the number of characters in the text and m is the number of
                             characters in the pattern
                space: O(k(n + x)) where k is the number of pattern segments and n is the number of characters in the
                       text and x is a fraction of the characters in the pattern
    error handling:
    '''
    txt = openFile(txtfile)
    pat = openFile(patfile)

    # O(m)
    segmented_pats, consecutive_wildcards = segment(pat)
    # O(k(n + x) + q)
    segmented_z_arr = getSegmentedZArr(segmented_pats, txt)

    i = 0
    segmented_pats_len = len(segmented_pats[i])
    j = segmented_pats_len + 1
    # consecutive_wildcards[0] is the number of text characters matching the pattern
    matches = consecutive_wildcards[0]
    previous = None
    output = []
    # when number of characters == 1, loop runs 1 time
    # when number of characters > 1, loop runs n times
    while j < segmented_pats_len + len(txt) + 1:
        if i != 0 and segmented_z_arr[i][j] != segmented_pats_len:
            # return to first non-wildcard segment to find matching text again
            # when subsequent text does not match subsequent non-wildcard segment
            j = previous + segmented_z_arr[0][previous]
            i = 0
            matches = 0
        elif segmented_z_arr[i][j] != segmented_pats_len:
            # go to the next character when text does not match first non-wildcard segment
            j += 1
            previous = j
        else:
            # current number of matching characters + number of characters in the first non-wildcard segment as text
            # matches
            matches += segmented_z_arr[i][j]
            # current number of matching characters + number of consecutive wildcards after the first non-wildcard
            # segment
            matches += consecutive_wildcards[matches]
            # go to the next unchecked character
            j += matches
            # in the next non-wildcard segment
            i += 1

            if i != len(segmented_pats):
                segmented_pats_len = len(segmented_pats[i])
            elif matches == len(pat):
                output += [previous - len(segmented_pats[0])]
                # go to the next unchecked character
                j = previous + segmented_z_arr[0][previous]
                # in the first non-wildcard segment to find subsequent matching pattern in text
                i = 0
                matches = 0
                previous = j
    writeFile('output_wildcard_matching.txt', output)
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

    wildcard_matching(txtfile, patfile)


if __name__ == '__main__':
    main()
    # wildcard_matching('txtfile2.txt', 'patfile2.txt')
