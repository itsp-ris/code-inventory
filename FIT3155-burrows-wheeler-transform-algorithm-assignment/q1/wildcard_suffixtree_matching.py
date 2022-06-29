'''
ID: 28390121
author: Priscilla Tham
Date: 10/05/2020
'''
import argparse as ap


class TreeNode:
    # once a leaf, always a leaf rule
    # all nodes end is equal to global end until branching is necessary
    end = 0

    def __init__(self, start=0, size=95):
        self.start = start
        # time and space complexity is constant
        self.child = [None] * size
        self.link = None

    def set_start(self, start):
        '''
        function modifies the default or initialised starting index of a node
        precondition:
        :param: start: the new starting index to replace with
        postcondition:
        :return:
        complexity: time: best and worst: O(k) where k = 1 is possible
        error handling:
        '''
        self.start = start

    def set_end(self, end):
        '''
        function modifies the ending index of a node from the global ending index
        precondition:
        :param: start: the new ending index to replace with
        postcondition:
        :return:
        complexity: time: best and worst: O(k) where k = 1 is possible
        error handling:
        '''
        self.end = end

    def set_link(self, node):
        '''
        function modifies the default link of a node
        precondition:
        :param: node: the new node to link with
        postcondition:
        :return:
        complexity: time: best and worst: O(k) where k = 1 is possible
        error handling:
        '''
        self.link = node


class Tree:

    def __init__(self, size=95):
        # always points to the root/head
        self.head = TreeNode(0)
        # root as the starting point in the next phase
        self.node = self.head

    def next(self, prefix_length, txt, j, offset):
        '''
        function updates pointer to the starting point of the next phase
        precondition:
        :param prefix_length: the offset from the starting index of a node
               txt: the text string
               j: the showstopper character position
               offset: the offset from the ascii value of a character which results to the position of the node
                        representing the character or substring starting from the character
        postcondition:
        :return:
        complexity: time: best and worst: O(k) where k = 1 is possible
                    space: O(k) where k = 1 is possible
        error handling:
        '''
        # suffix link rule
        # prefix length > 1 indicates that the characters from the showstopper to the preceding character of the
        # current character already exist in tree
        if prefix_length > 1:
            # links to the next character in text string
            # then node representing the next character will be the starting point in the next phase
            # avoid revisiting preceding nodes from the root
            self.node.set_link(self.head.child[ord(txt[j + 1]) - offset])
        else:
            # links to the root
            # then the root will be the starting point in the next phase
            # allow addition of the current character to the tree if has yet to exist
            self.node.set_link(self.head)

    def make_subtree(self, txt, node, prefix_length, offset):
        '''
        function creates the subtree of a node from the tree
        precondition:
        :param: txt: the text string the tree is built based on
                node: the node to create a subtree
                prefix_length: the offset from the starting index of a node which results to the (new) ending index
                               upon addition
                offset: the offset from the ascii value of a character which results to the position of the node
                        representing the character or substring starting from the character
        postcondition: global ending index of all other nodes is not modified
        :return: the subtree
        complexity: time: best and worst: O(k) where k = 1 is possible
                    space: O(n) where n is the number of nodes in the subtree
        error handling:
        '''
        subtree = Tree()
        index = ord(txt[node.start]) - offset
        subtree.node.child[index] = TreeNode(node.start)
        # replace global end with end of substring before the next character
        # then node end is not equal to global end from this point
        subtree.node.child[index].set_end(node.start + prefix_length - 1)
        subtree.node.child[index].set_link(node.link)
        subtree.node = subtree.node.child[index]
        return subtree

    def insert(self, txt, i, j, offset):
        '''
        function inserts a node to the current position of the tree
        precondition:
        :param: txt: the text string the tree is build based on
                i: the position of the character in the text string to be represented by the inserted node
                j: the position of the character or the starting character of a substring in the text string
                   represented by the current node
                offset: the offset from the ascii value of a character which results to the position of the node
                        representing the character or substring starting from the character
        postcondition: the nodes are storing starting and ending position of a substring rather than their characters
        :return: boolean
        complexity: time: best and worst: O(n) where n is the number of nodes
                    space: O(n) where n is the number of nodes
        error handling:
        '''
        index = ord(txt[i]) - offset
        # showstopper rule
        if self.node != self.head:
            parent = self.head
            node = self.node
            prefix_length = i - j

            # find a child node representing the preceding substring of the current character
            # when number of nodes == 1, loop runs 1 time
            # when number of nodes > 1, loop runs n times
            while node.end - node.start + 1 < prefix_length:
                parent = node
                prefix_length -= node.end - node.start + 1
                # skip count rule
                # skip to the next preceding substring
                node = node.child[ord(txt[i - prefix_length]) - offset]

            substring_length = node.end - node.start + 1
            # branch to add the current character to the current (child) node representing the preceding substring of
            # the current character if does not exist
            if substring_length > prefix_length and txt[node.start + prefix_length] != txt[i]:
                # build a subtree of the current (child) node before adding the branch node
                # avoid replacing existing branches
                subtree = self.make_subtree(txt, node, prefix_length, offset)
                # replace current node with the built subtree
                parent.child[ord(txt[node.start]) - offset] = subtree.node
                subtree.node.child[index] = TreeNode(i)
                index = ord(txt[node.start + prefix_length]) - offset
                subtree.node.child[index] = node
                subtree.node.child[index].set_start(node.start + prefix_length)
                # suffix linked node as the starting point in the next phase
                self.next(i - j, txt, j, offset)
                self.node = self.node.link
                return True
            # add node representing the current character to the current (child) node representing the preceding
            # substring of the current character if does not exist
            elif substring_length == prefix_length and not node.child[index]:
                node.child[index] = TreeNode(i)
                # suffix linked node as the starting point in the next phase
                self.next(i - j, txt, j, offset)
                self.node = self.node.link
                return True
            # suffix linked node as the starting point in the next phase
            self.next(i - j, txt, j, offset)
            return False
        else:
            # add node if current character does not exist in tree
            if not self.node.child[index]:
                self.node.child[index] = TreeNode(j)
                self.node.child[index].set_link(self.head)
                return True
            # showstopper rule
            # node as the starting point in the next phase if character exist in tree
            self.node = self.node.child[index]
            self.node.set_link(self.head)
            return False


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
    string = ''
    for i in range(len(output)):
        string += str(output[i]) + '\n'
    with open(filename, 'w') as file:
        file.write(string)
    return


def count_sort(output, txt_length):
    '''
    function sorts items using counting sort
    precondition:
    :param: output: the items to sort
            txt_length: the maximum number of items
            sorted_output: the array to store sorted items
    postcondition:
    :return: the sorted items array
    complexity: time: best and worst: O(k) where k is the number of characters in text
    space: O(k) where k is the number of characters in text
    '''
    matching_index = [0 for _ in range(txt_length)]
    # when length of output == 1, loop runs 1 time
    # when length of output > 1, loop runs p times
    for i in range(len(output)):
        matching_index[output[i]] += 1

    sorted_output = []
    # when number of characters == 1, loop runs 1 time
    # when number of characters > 1, loop runs k times
    for j in range(txt_length):
        if matching_index[j] > 0:
            sorted_output += [j + 1]
    return sorted_output


def get_remaining_match(output, node, txt, pat):
    '''
    functions finds the remaining matching pattern in the text using the suffix tree
    precondition:
    :param: output: the array to be appended of positions in the text string where the pattern exists
            node: the current position in the tree which represents the current substring in the text to be
                  compared with the pattern
            txt: the text string
            pat: the pattern string
    postcondition:
    :return:
    complexity: time: best and worst: O(k) where k = 1 is possible
                space:
    error handling:
    '''
    printables = 95
    i = 0
    while i < printables:
        if node.child[i]:
            if txt[node.child[i].end] != '$':
                get_remaining_match(output, node.child[i], txt, pat)
            else:
                output += [node.child[i].start - len(pat)]
        i += 1
    return


def recursive_wildcard_suffixtree_matching(output, node, txt, pat, i, index, offset):
    '''
    function performs pattern matching using the suffix tree
    precondition:
    :param  output: the array to be appended of positions in the text string where the pattern exists
            node: the current position in the tree which represents the current substring in the text to be
                  compared with the pattern
            txt: the text string
            pat: the pattern string
            i: the position of a character in the pattern
            index: the position of a character or the starting character of a substring in the text
            offset: the offset from the ascii value of a character which results to the position of the node
                    representing the character or substring starting from the character
    postcondition:
    :return:
    complexity: time: best and worst: O(n + m) where n is the number of nodes and m is the number of characters in
                                      the pattern string
                space: O(p) where p is the length of output
    error handling:
    '''
    printables = 95
    pat_length = len(pat)
    # find the deepest node
    if node.child[index] and i == 0:
        recursive_wildcard_suffixtree_matching(output, node.child[index], txt, pat, i, index, offset)

    if node.child[index]:
        substring_length = node.child[index].end - node.child[index].start + 1
        j = 1
        # when number of characters == 1, loop runs 1 time
        # when number of characters > 1, loop runs m times
        while j < substring_length and i + j < pat_length:
            # pattern does not exist if the current character does not match
            # do not need to check the other nodes due to the suffix tree property of lining up substrings with the
            # same prefix
            if pat[i + j] != '?' and pat[i + j] != txt[node.child[index].start + j]:
                return
            j += 1

        if not i + j < pat_length:
            output += [node.child[index].start - i]
            if i == 0: get_remaining_match(output, node.child[index], txt, pat)
            return
        # move to the next character of the pattern in the child node if exist
        recursive_wildcard_suffixtree_matching(output, node.child[index], txt, pat, i + j, ord(pat[i + j]) - offset,
                                               offset)
        return
    elif pat[i] == '?':
        k = 0
        # find a child node to compare the next character of the pattern as the current character is a wildcard
        while k < printables:
            if node.child[k]:
                # move to the next character of the pattern in the child node if exist
                recursive_wildcard_suffixtree_matching(output, node, txt, pat, i, k, offset)
            k += 1
        return
    # pattern does not exist if the current character does not match
    # note that wildcard always match
    # do not need to check the other nodes due to the suffix tree property of lining up substrings with the
    # same prefix
    return


def get_tree(txt, offset):
    '''
    function builds a suffix tree
    precondition:
    :param  txt: the text string the tree is built based on
            offset: the offset from the ascii value of a character which results to the position of the node
                    representing the character or substring starting from the character
    postcondition:
    :return:
    complexity: time: best and worst: O(n) where n is the number of nodes
                space: O(n) where n is the number of nodes
    error handling:
    '''
    tree = Tree()
    i = 0
    j = 0
    # when all characters is different, loop runs n times
    # otherwise, loop runs 2n times
    while i < len(txt):
        TreeNode.end = i
        if not tree.insert(txt, i, j, offset):
            # showstopper rule
            if i != len(txt) - 1: i += 1
        else:
            # subsequent showstopper rule
            if i - j != 0:
                j += 1
            else:
                i += 1
                j += 1
    return tree


def open_file(filename):
    '''
    function opens a file
    precondition:
    :param  filename: the name of the file to open
    postcondition: the content of the file is not modified
    :return: the content of the file
    complexity: time: best and worst: O(q) where q is the number of characters in the file
                space: O(q) where q is the number of characters in the file
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


def wildcard_suffixtree_matching(txtfile, patfile):
    '''
    function builds a suffix tree and performs pattern matching using it
    precondition:
    :param  txtfile: the name of the file containing the text string
            patfile: the name of the file containing the pattern string
    postcondition: the content of the files are not modified
    :return:
    complexity: time: best and worst: O(n + m) where n is the number of nodes and m is the number of characters in
                                      the pattern string
                space: O(n) where n is the number of nodes
    error handling:
    '''
    offset = 32
    txt = open_file(txtfile) + '$'
    pat = open_file(patfile)

    pat_length = len(pat)
    txt_length = len(txt)
    # O(n)
    tree = get_tree(txt, offset)
    output = []
    if pat_length > 1:
        # O(n + m)
        recursive_wildcard_suffixtree_matching(output, tree.head, txt, pat, 0, ord(pat[0]) - offset, offset)
        output = count_sort(output, txt_length)
    elif pat_length == 1:
        # when number of characters == 1, loop runs 1 time
        # when number of characters > 1, loop runs k times
        for i in range(txt_length):
            if txt[i] == pat[0] or pat[0] == '?':
                output += [i]
    write_file('output_wildcard_matching.txt', output)
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

    wildcard_suffixtree_matching(txtfile, patfile)


if __name__ == "__main__":
    main()