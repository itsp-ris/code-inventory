'''
ID: 28390121
author: Priscilla Tham
Date: 15.05.2018
'''

from task3 import LinkedList
from atask3 import HashTableLinear


class HashTableSeparateChaining(HashTableLinear):
    def __init__(self, size, base):
        HashTableLinear.__init__(self, size, base)

    def __str__(self):
        '''
        function concatenates (key, value) information in the hash table as a string
        precondition:
        :param:
        postcondition: (key, value) pair in the hash table are all joined with a new line
        :return: a string type
        complexity: best: O(1) when the size of the hash table == 1
                    worst: O(N) where N is the size of the hash table
        '''
        res = ''
        # when the only (key, value) pair is at the first position, the loop runs 1 times
        # when the (key, value) pair is at the last position, the loop runs n time
        for i in range(self.table_size):
            if self.array[i] is not None:
                node = self.array[i].head
                while node is not None:
                    res += '(' + str(node.item[0]) + ', ' + str(node.item[1]) + ')' + '\n'
                    node = node.next
        return res

    def __getitem__(self, key):
        '''
        function retrieves data of the associated key from hash table
        precondition: hash table is not empty
        :param: key: key input from the user
        postcondition:
        :return: data of the key
        complexity: best: O(1) when the key is at the first position in the the hash table
                    worst: O(N) where N is the size of the hash table
        '''
        position = self.hash_value(key)
        node = self.array[position].head
        # when the key cannot be found, the loop runs n times
        for _ in range(len(self.array[position])):
            if node.item[0] == key:
                return node.item[1]
        raise KeyError

    def __setitem__(self, key, item):
        '''
        function inputs or updates the (key, value) information in the hash table
        precondition:
        :param: key: key input from the user
                value: data associated to the key the user input
        postcondition: data associated to the key is overwritten when updating
        :return:
        complexity: best: O(1)
                    worst: O(N) where N it the size of the hash table
        '''
        # when the empty space to insert the (key, value) information is in the first position of the hash table,
        # the loop runs 1 time
        position = self.hash_value(key)
        if self.array[position] is None:
            self.array[position] = LinkedList()
            self.array[position].append((key, item))
        else:
            node = self.array[position].head
            # when the key to be updated is in the first position of the hash table,
            # the loop runs 1 time
            # when the key to be updated is in the last position of the hash table,
            # the loop runs n times
            while node is not None:
                if node.item[0] == key:
                    node.item = (key, item)
                    return
                node = node.next
                self.probe_length += 1
            self.array[position].append((key, item))
            self.collision += 1


if __name__ == '__main__':
    my_table = HashTableSeparateChaining(10, 3)
    my_table["Eva"] = "Eva"
    my_table["Amy"] = "Amy"
    my_table["Tim"] = "Tim"
    my_table["Ron"] = "Ron"
    my_table["Jan"] = "Jan"
    my_table["Kim"] = "Kim"
    my_table["Dot"] = "Dot"
    my_table["Ann"] = "Ann"
    my_table["Jim"] = "Jim"
    my_table["Jon"] = "Jon"
    my_table["Amm"] = "Amm"
    my_table["Pij"] = "Pij"
    my_table["Ben"] = "Ben"
    print(my_table['Eva'])
    print(my_table.collision)
    print(my_table.probe_length)