'''
ID: 28390121
author: Priscilla Tham
Date: 15.05.2018
'''

from referential_array import build_array


class HashTable:
    def __init__(self, size, base):
        self.count = 0
        self.table_size = size
        self.a = base
        self.array = build_array(self.table_size)

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

        for i in range(self.table_size):
            if self.array[i] is not None:
                res += '(' + str(self.array[i][0]) + ', ' + str(self.array[i][1]) + ')'+'\n'
        return res

    def __len__(self):
        '''
        function counts the number of (key, value) pair in the hash table
        precondition:
        :param:
        postcondition:
        :return: number of (key, value) pair in the hash table
        complexity: best and worst: O(1)
        '''
        return self.count

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

        for i in range(self.table_size):
            # when the key cannot be found, the loop runs n times
            if self.array[position] is None:
                raise KeyError
            if self.array[position][0] == key:
                return self.array[position][1]
            position = (position + 1) % self.table_size
        raise KeyError

    def __setitem__(self, key, value):
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
        if self.count == self.table_size:
            raise Exception

        position = self.hash_value(key)

        # when the empty space to insert the (key, value) information is in the first position of the hash table,
        # the loop runs 1 time
        for _ in range(self.table_size):
            # when the empty space to insert the (key, value) information is in the first position of the hash table,
            # the loop runs 1 time
            # when the empty space to insert the (key, value) information is in the last position of the hash table,
            # the loop runs n times
            if self.array[position] is None:
                self.array[position] = (key, value)
                self.count += 1
                return
            # when the key to be updated is in the first position of the hash table,
            # the loop runs 1 time
            # when the key to be updated is in the last position of the hash table,
            # the loop runs n times
            elif self.array[position][0] == key:
                self.array[position] = (key, value)
                return
            else:
                position = (position + 1) % self.table_size

    def __contains__(self, key):
        '''
        function determines if the key exist in the hash table
        precondition: hash table is not empty
        :param: key: the key the user wants to check
        postcondition:
        :return: boolean value: True if key is in the hash table
                                False if key is not in the hash table
        complexity: best: O(1) when the key is at the first position in the hash table
                    worst: O(N) where N is the size of the hash table
        '''
        try:
            if self[key]:
                return True
        # when the key cannot be found, __getitem__ function loop runs n times
        except KeyError:
            return False

    def hash_value(self, key):
        '''
        function calculates the position of the key in the hash table
        precondition:
        :param: key: the key the user wants to insert into the hash table
        postcondition:
        :return: the value of h; the position
        complexity: best: O(1) where the length of the key is 1
                    worst: O(N) where N is the length of the key
        '''
        a = self.a
        h = 0
        for c in key:
            h = (h*a + ord(c)) % self.table_size
        return h


if __name__ == '__main__':
    table = HashTable(10, 3)
    my_table = HashTable(10, 3)
    my_table["Eva"] = "Eva"
    my_table["Amy"] = "Amy"
    my_table["Tim"] = "Tim"
    my_table["Ron"] = "Ron"
    my_table["Jan"] = "Jan"
    # my_table["Kim"] = "Kim"
    # my_table["Dot"] = "Dot"
    # my_table["Ann"] = "Ann"
    # my_table["Jim"] = "Jim"
    # my_table["Jon"] = "Jon"
    # my_table["Amm"] = "Amm"
    # my_table["Pij"] = "Pij"
    my_table["Ben"] = "Ben"
    print(my_table)
