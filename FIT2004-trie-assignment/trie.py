'''
ID: 28390121
author: Priscilla Tham
Date: 03.05.2019
'''

class TrieNode:

    def __init__(self, size=62):
        self.array = []
        # time and space complexity is constant
        self.child = [None]*size


class Trie:

    def __init__(self, size=62):
        # always points to the root/head
        self.head = TrieNode(size)
        # points to the current position
        self.node = self.head

    def _get_index(self, char):
        '''
        function calculates the position of the node for the character
        precondition: size of trie node must be 52 in case of inserting alphabets
        :param: char: character to be inserted
        postcondition:
        :return: integer in the range of 0 to the size of trie node as the position of the node for the character
        complexity: time: best and worst: O(p) where p = 1 is possible
                    space:
        error handling:
        '''
        try:
            return int(char)
        # should it gives an error, the character is of type alphabets, therefore calculation is done by using
        # ASCII value
        # an addition of 26 (letters) if the character is lowercase taking into consideration of uppercase letters
        except ValueError:
            if char.islower():
                return ord(char) - ord('a') + 26
            if char.isupper():
                return ord(char) - ord('A')

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
        index = self._get_index(char)
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
        try:
            # when number of characters == 1, loop runs 1 time
            # when number of characters > 1, loop runs m times
            for i in range(len(key)):
                index = self._get_index(key[i])
                if not node.child[index]:
                    return []
                node = node.child[index]
            return node.array
        # should it gives an error, the item is of type integer
        except TypeError:
            index = self._get_index(key)
            if not node.child[index]:
                return []
            node = node.child[index]
        return node.array

def query(filename, id_prefix, last_name_prefix):
    '''
    function finds pairs of data containing the id prefix and last name prefix the user input
    precondition: the file is not empty and each data is in a new line;
                  data ids consists of integers only and data last names consists of alphabets only
    :param: filename: the name of the file containing the data
            id_prefix: positive integers
            last_name_prefix: letters
    postcondition: the file is not modified
    :return: the indices associated to the data containing the id prefix and last name prefix
    complexity: time: best: O(T) + O(l)/O(T) + O(k) where T is the number of characters in all ids
                      and all last names, k is the length of id_prefix and l is the length of last_name_prefix
                      worst: O(T) + O(k + l + nk + nl) where nk is the number of records matching id_prefix and
                      nl is the number of records matching last_name prefix
                space: O(T + nm) where T is the number of characters in all ids and all last names, n is the
                number of data associated to all ids and all last names and m is the maximum number of
                characters (either id or last name) per data
    error handling: return empty list if file does not exist
    '''
    try:
        with open(filename, 'r', encoding='UTF-8') as file:
            context = file.read()

        n = len(context)
        if n == 0:
            return []

        data = ''
        sepCount = 0
        # when number of characters == 1, loop runs 1 time
        # when number of characters > 1, loop runs p times
        # where p is the total number of characters
        for i in range(n):
            if context[i] != ' ' and (sepCount == 1 or sepCount == 3):
                data += context[i]
            if context[i] == ' ':
                sepCount += 1
                if sepCount == 2:
                    data += ' '
            if context[i] == '\n':
                data += '\n'
                sepCount = 0

        # further nodes/child nodes are only created during insertion
        idTrie = Trie(10)
        lnTrie = Trie(52)

        index = int(context[0])
        endFlag = 0
        # when number of characters == 1, loop runs 1 time
        # when number of characters > 1, loop runs T times
        # where T is the number of characters in all id and all last names
        # O(T)
        for j in range(len(data)):
            if data[j] == ' ':
                # points the node to the root/head for each new data
                idTrie.node = idTrie.head
                endFlag = 1
            elif data[j] == '\n':
                # points the node to the root/head for each new data
                lnTrie.node = lnTrie.head
                endFlag = 0
                index += 1
            elif endFlag != 1:
                # creates the node for the character
                # O(1)
                idTrie.insert(data[j])
                # appends the index associated to the data to the array in the node created
                # O(1)
                idTrie.append(index)
            else:
                # creates the node for the character
                # O(1)
                lnTrie.insert(data[j])
                # appends the index associated to the data to the array in the node created
                # O(1)
                lnTrie.append(index)

        # if both prefix is empty, return all indices of the database
        if len(id_prefix) == 0 and len(last_name_prefix) == 0:
            return list(range(0, index + 1))
        else:
            # search loop runs according to the length of id_prefix, k
            # O(k)
            matchedID = idTrie.search(id_prefix)
            # search loop runs according to the length of last_name_prefix, l
            # O(l)
            matchedLn = lnTrie.search(last_name_prefix)

            # if either is empty, return the matching indices for the non empty prefix
            if len(id_prefix) == 0:
                return matchedLn
            elif len(last_name_prefix) == 0:
                return matchedID
            else:
                # further nodes/child nodes are only created during insertion
                pairTrie = Trie(index+1)

                pairs = []
                # when number of matching ids == 1, loop runs 1 time
                # when number of matching ids > 1, loop runs nk times
                # O(nk)
                # best case when there is no matching ids and matching last names
                for k in range(len(matchedID)):
                    # creates the node for the character
                    # O(1)
                    pairTrie.insert(matchedID[k])
                    # appends the index associated to the data to the array in the node created
                    # O(1)
                    pairTrie.append(matchedID[k])
                    # points the node to the root/head for each new data
                    pairTrie.node = pairTrie.head

                # when number of matching last names == 1, loop runs 1 time
                # when number of matching last names > 1, loop runs nl times
                # O(nl)
                # best case when there is no matching ids and matching last names
                for m in range(len(matchedLn)):
                    # search loop runs in constant time as items in matchedLn are all integers
                    # O(1)
                    pairs += pairTrie.search(matchedLn[m])
                return pairs
    except FileNotFoundError:
        return []

def reverseSubstrings(filename):
    '''
    function finds substrings whose reverse appears in a string
    precondition: the file is not empty and there is only one string
    :param: filename: the name of the file which contains the string
    postcondition: the file is not modified
    :return: the pair of substrings and reverse of the substrings in the strings with its starting position
             in the string
    complexity: time: best and worst: O(K^2 + P) where K is the total number of characters in the input string and P
                      is the total length of all substrings whose reverse appears in the string.
                space: O(K^2 + P)
    error handling: return empty list if file does not exist
    '''
    try:
        with open(filename, 'r', encoding='UTF-8') as file:
            context = file.read()

        n = len(context)
        if n == 0:
            return []

        # takes the space of O(M)
        # where M is the total length of all substrings
        substrings = ''
        # takes the space of O(N)
        # where N is the number of substring
        indexes = []
        i = 2
        j = 0
        # loop runs K-1 times
        # where K is the total number of characters in the input string
        # O(K^2)
        while i < n+1:
            if j != n:
                # string/list slicing is O(K)
                # where K is the maximum number of characters to slice
                item = context[j:j+i]
                if len(item) >= i:
                    substrings += item
                    indexes += [j]
                    substrings += ' '
                j += 1
            else:
                j = 0
                i += 1

        # further nodes/child nodes are only created during insertion
        trie = Trie()

        n = 0
        # takes the space of O(K)
        visited = [None]*len(context)

        # when number of characters == 1, loop runs 1 time
        # when number of characters > 1, loop runs M times
        # where M is the total length of all substrings
        # O(M)
        for k in range(len(substrings)):
            if substrings[k] == ' ':
                visited[indexes[n]] = indexes[n]
                n += 1
                # points the node to the root/head for each new data
                trie.node = trie.head
            else:
                # creates the node for the character
                # O(1)
                trie.insert(substrings[k])
                if len(trie.node.array) <= 0:
                    # appends the index/position of the character in the string to the array in the node created
                    # O(1)
                    trie.append(indexes[n])
                elif visited[indexes[n]] is None:
                    # appends the index/position of the character in the string to the array in the node created
                    # O(1)
                    trie.append(indexes[n])

        # when number of characters == 1, system look for whitespace(s) once
        # when number of characters > 1, system look for whitespace(s) N times
        substrings = substrings.split()

        # takes the space of O(KNp)
        # where K is the maximum number of characters in a substring and Np is the number of substrings whose reverse
        # appears in the string
        output = []
        n = 0
        # when number of characters == 1, loop runs 1 time
        # when number of characters > 1, loop runs N times
        # where N is the number of substrings
        # O(KN)
        for m in range(len(substrings)):
            # search loop runs according to the length of substring, T
            # O(K) where T = K
            array = trie.search(substrings[m][::-1])
            if array:
                output += [[substrings[m], indexes[n]]]
            n += 1
        return output
    except FileNotFoundError:
        return []

if __name__ == '__main__':
    print(query('test.txt', '123', 'Brady'))
    # print(query('Database.txt', '0', 'Will'))
    print(reverseSubstrings('T2_S3.txt'))
    # print(reverseSubstrings('T2_S4.txt'))
    # print(reverseSubstrings('T2_S5.txt'))