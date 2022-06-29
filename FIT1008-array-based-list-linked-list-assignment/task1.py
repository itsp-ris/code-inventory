'''
ID: 28390121
author: Priscilla Tham
Date: 28.04.2018
'''
from referential_array import build_array

class ListIterator:
    def __init__(self, array, count):
        self.counter = 0
        self.array = array
        self.count = count

    def __iter__(self):
        '''
        function returns an iterator object
        precondition:
        :param:
        postcondition:
        :return: the address of iterator object
        complexity: best: O(1) when length of list == 1
                    worst: O(N) where N is the length of list
        '''
        return self

    def __next__(self):
        '''
        function moves iterator pointer to the next item in the list
        preconditon:
        :param:
        postconditon:
        :return: the item at the current position of the iterator pointer
        complexity: best: O(1) when length of list == 1
                    worst: O(N) where N is the length of list
        '''
        if self.counter == self.count:
            raise StopIteration
        else:
            item_required = self.array[self.counter]
            self.counter += 1
        return item_required

class Array:
    def __init__(self, size = 50):
        '''
        function build an empty array
        precondition: decimal_number: integer <= 50
        :param: size: size input of the array from the user
        postcondition: empty array of size as inputted, or 50 if size is not provided
        :return:
        complexity: best and worst: O(1)
        '''
        assert size <= 50 and size > 0, 'Size must be positive and maximum size is 50.'
        self.array = build_array(size)
        self.count = 0

    def __str__(self):
        '''
        function concatenates items in the list as a string
        precondition:
        :param:
        postcondition: items in the list are all joined with a new line
        :return: a string type
        complexity: best: O(1) for length of list == 1
                    worst: O(N) where N is the length of list
        '''
        string = ''

        # when len(list) == 1, loop runs 1 time
        for i in range(len(self)):
            string += str(self.array[i]) + '\n'
        return string

    def __len__(self):
        '''
        function counts the number of items in the list
        precondition:
        :param:
        postcondition:
        :return: number of items in the list
        complexity: best and worst: O(1)
        '''
        return self.count

    def __contains__(self, item):
        '''
        function determines if item exist in the list
        precondition: list if not empty
        :param: item: the item user wants to check
        postcondition:
        :return: boolean value: True if item is in the list
                                False if item is not in the list
        complexity: best and worst: O(1)
        '''
        if item in self.array:
            return True
        return False

    def __getitem__(self, index):
        '''
        function retrieves item from the list at position index
        precondition: list is not empty
        :param: index: position input from the user
        postcondition:
        :return: item at position index of the list
        complexity: best and worst: O(1)
        '''
        if index >= len(self) or index < -len(self):
            raise IndexError

        if index >= 0:
            return self.array[index]
        else:
            return self.array[len(self) + index]

    def __setitem__(self, index, item):
        '''
        function replaces item at position index of the list
        precondition:
        :param: index: position input from the user
                item: the item the user want to replace with
        postcondition: item at position index of the list is overwritten
        :return:
        complexity: best and worst: O(1)
        '''
        assert not self.is_empty(), 'List is empty.'
        if index >= len(self) or index < -len(self):
            raise IndexError

        if index >= 0:
            self.array[index] = item
        else:
            self.array[len(self) + index] = item

    def __eq__(self, other):
        '''
        function compares between two list
        precondition:
        :param: other: another list to compare with
        postcondition:
        :return: boolean value: True if both lists are the same
                                False if the both lists are different
        complexity: best: O(1) when length of list != length of other
                    worst: O(N) where N is the length of list
        '''
        if len(self) == len(other):
            for i in range(len(self)):
                if self.array[i] != other[i]:
                    return False
        else:
            return False
        return True

    def __iter__(self):
        '''
        function calls an iterator class
        precondition:
        :param:
        postconditon:
        :return:
        complexity: best: O(1) when length of list == 1
                    worst: O(N) where N is the length of list
        '''
        # when len(list) == 1, only calls itself once
        return ListIterator(self.array, self.count) # when len(list) == 1, only calls itself once

    def is_full(self):
        '''
        function checks if the array is full
        precondition:
        :param:
        postcondition:
        :return: boolean value: True if array is full
                                False if array has space
        complexity: best and worst: O(1)
        '''
        return len(self) >= len(self.array)

    def is_empty(self):
        '''
        function checks if the array is empty
        precondition:
        :param:
        postcondition:
        :return: boolean value: True if array is empty
                                False if array contains items
        complexity: best and worst: O(1)
        '''
        return len(self) == 0

    def append(self, item):
        '''
        function appends item into array
        precondition:
        :param: item: the item the user wants to append into the array
        postcondition: array space decreases by one
        :return:
        complexity: best and worst: O(1)
        '''
        assert not self.is_full(), 'List is full.'
        self.array[self.count] = item
        self.count += 1


    def insert(self, index, item):
        '''
        function inserts item into list at position index
        precondition:
        :param: index: position input from the user
                item: the item the user wants to insert into the list
        postcondition: array space decreases by one
        :return:
        complexity: best: O(1) when the index is -1
                    worst: O(N) where N is the length of list and index is 0
        '''
        if index >= len(self) or index < -len(self):
            raise IndexError

        if index >= 0:
            # when index == 0, loop runs n-1 times
            for i in range(len(self), index, -1):
                self.array[i] = self.array[i - 1]
            self.array[index] = item
        else:
            # when index == -1, loop runs 1 time
            for i in range(len(self), len(self) + index , -1):
                self.array[i] = self.array[i - 1]
            self.array[len(self) + index] = item
        self.count += 1

    def remove(self, item):
        '''
        function removes item from the list
        precondition: list is not empty
        :param: item: the item the user wants to remove from the list
        postcondition: array space increases by one
        :return:
        complexity: best and worst: O(N) where N is the length of list
        '''
        if item not in self.array:
            raise ValueError

        # when item is the first, second loop runs n times
        # when item is the last, second loop runs 1 time but first loop runs n times
        for i in range(len(self)):
            if self.array[i] == item:
                break

        for j in range(i, len(self) - 1):
            self.array[j] = self.array[j + 1]
        self.count -= 1

    def delete(self, index):
        '''
        function deletes item from list at position index
        precondition:
        :param: index: position input from the user
        postcondition: array space increases by one
        :return:
        complexity: best: O(1) when index is -1
                    worst: O(N) where N is the length of list and index is 0
        '''
        if index >= len(self) or index < -len(self):
            raise IndexError

        if index >= 0:
            # when index = 0, loop runs n-1 times
            for i in range(index, len(self) - 1):
                self.array[i] = self.array[i + 1]
        else:
            # when index is -1, loop runs 1 time
            for i in range(index + len(self), len(self) - 1):
                self.array[i] = self.array[i + 1]
        self.count -= 1

    def sort(self, reverse):
        '''
        function sorts items in the list
        precondition: list is not empty
        :param: reverse: True for ascending order or False for descending order
        postcondition: list is sorted
        :return:
        complexity: best and worst: O(N**2) where N is the length of list
        '''
        if reverse == False:
            # when list is sorted, both first and second loop still runs n times
            for i in range(len(self)):
                min = i
                for j in range(i + 1, len(self)):
                    if self.array[j] < self.array[min]:
                        min = j
                temp = self.array[i]
                self.array[i] = self.array[min]
                self.array[min] = temp

        elif reverse == True:
            # when list is sorted, both first and second loop still runs n times
            for i in range(len(self)):
                max = i
                for j in range(i + 1, len(self)):
                    if self.array[j] > self.array[max]:
                        max = j
                temp = self.array[i]
                self.array[i] = self.array[max]
                self.array[max] = temp


if __name__ == '__main__':
    while True:
        try:
            size = int(input('Enter size: '))
            array = Array(size)
            break
        except ValueError:
            print('Enter numbers only.')
        except AssertionError as e:
            print(e)