'''
ID: 28390121
author: Priscilla Tham
Date: 15.05.2018
'''
from atask1 import HashTable


class HashTableLinear(HashTable):
    def __init__(self, size, base):
        HashTable.__init__(self, size, base)
        self.collision = 0
        self.probe_length = 0

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

        # when the key has yet to be inserted/updated even after probing until the end of the hash table,
        # the loop runs n times
        for i in range(self.table_size):
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
                if i == 0:
                    self.collision += 1
                position = (position + 1) % self.table_size
                self.probe_length += 1

    def track_load(self):
        '''
        function calculates the load factor
        precondition: the size of the hash table is more than 0
        :param:
        postcondition:
        :return: the value of the number of (key, value) pairs in the hash table / the size of the hash table
        complexity: best and worst: O(1)
        '''
        return self.count / self.table_size

    def track_avg_probe_length(self):
        '''
        function calculates the average probe length
        precondition: the number of (key, value) pairs in the hash table is more than 0
        :param:
        postcondition:
        :return: the value of the total probe Length / the number of (key, value) pair in the hash table
        complexity: best and worst: O(1)
        '''
        assert self.count > 0, 'Cannot divide by zero.'
        return self.probe_length / self.count


if __name__ == '__main__':
    my_table = HashTableLinear(10, 3)
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
    # my_table["Amm"] = "Amm"
    # my_table["Pij"] = "Pij"
    # my_table["Ben"] = "Ben"
    print(my_table)
    print(my_table.collision)
    print(my_table.track_load())
    print(my_table.track_avg_probe_length())
    print(my_table.probe_length)
