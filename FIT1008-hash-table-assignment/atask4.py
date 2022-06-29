'''
ID: 28390121
author: Priscilla Tham
Date: 15.05.2018
'''

from atask3 import HashTableLinear
from referential_array import build_array


class ListIterator:
    def __init__(self, array, size):
        self.counter = 0
        self.array = array
        self.table_size = size

    def __iter__(self):
        '''
        function returns an iterator object
        precondition:
        :param:
        postcondition:
        :return: the address of iterator object
        complexity: best: O(1) when the size of the hash table == 1
                    worst: O(N) where N is the size of the hash table
        '''
        return self

    def __next__(self):
        '''
        function moves iterator pointer to the next data in the hash table
        preconditon:
        :param:
        postconditon:
        :return: the data at the current position of the iterator pointer
        complexity: best: O(1) when the size of the hash table == 1
                    worst: O(N) where N is the size of the hash table
        '''
        if self.counter == self.table_size:
            raise StopIteration
        while self.counter < self.table_size:
            if self.array[self.counter] is not None:
                item_required = self.array[self.counter]
                self.counter += 1
                return item_required
            self.counter += 1
        raise StopIteration


class HashTableQuadratic(HashTableLinear):
    def __init__(self, size, base):
        HashTableLinear.__init__(self, size, base)

    def __iter__(self):
        '''
        function calls an iterator class
        precondition:
        :param:
        postconditon:
        :return:
        complexity: best: O(1) when size of the hash table == 1
                    worst: O(N) where N is the size of the hash table
        '''
        # when len(list) == 1, only calls itself once
        return ListIterator(self.array, self.table_size)

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

        i = 1

        # when the key cannot be found, the loop runs n times
        for j in range(self.table_size):
            if self.array[position] is None:
                raise KeyError
            if self.array[position][0] == key:
                return self.array[position][1]
            position = (self.hash_value(key) + i**2) % self.table_size
            i += 1
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
        if self.track_load() > 2/3:
            self.rehash()

        position = self.hash_value(key)

        i = 1

        # when the key has yet to be inserted/updated even after probing until the end of the hash table,
        # the loop runs n times
        for j in range(self.table_size):
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
                if j == 0:
                    self.collision += 1
                position = (self.hash_value(key) + i**2) % self.table_size
                self.probe_length += 1
                i += 1

        self.rehash()
        self.__setitem__(key, value)


    def rehash(self):
        '''
        function resizes hash table
        precondition: hash table is filled more than 2/3 of its size or there is no possible space to insert the key
        :param:
        postcondition: the (key, value) information is still retained in the hash table
        :return: address of caller
        complexity: best: O(N) where N is the size of the hash table
                    worst: O(N^2) where N is the size of the hash table
        '''
        temp = self.array
        self.count = 0
        self.table_size = self.table_size*2 + 1
        self.array = build_array(self.table_size)

        # __getitem__ function called runs n times to check the whole hash table
        # __setitem__ function called runs 1 time if the position to insert the key is in the first position
        # __setitem__ function called runs n times if the position to insert the key is in the last position
        for i in range(len(temp)):
            if temp[i] is not None:
                self[temp[i][0]] = temp[i][1]
        return


if __name__ == '__main__':
    size = int(input('Enter size: '))
    my_table = HashTableQuadratic(10, 3)
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
    print(my_table)
    print(my_table.collision)
    print(my_table.track_avg_probe_length())
    print(my_table.track_load())
