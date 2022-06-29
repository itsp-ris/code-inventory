'''
ID: 28390121
author: Priscilla Tham
Date: 28.04.2018
'''
from referential_array import build_array
from Node import Node

class ListIterator:
    def __init__(self, head):
        self.current = head

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
        if self.current is None:
            raise StopIteration
        else:
            item_required = self.current
            self.current = self.current.next
        return item_required


class LinkedList:
    def __init__(self):
        self.head = None
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

        node = self.head
        # when len(list) == 1, loop runs 1 time
        while node is not None:
            string += str(node.item) + '\n'
            node = node.next
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
        complexity: best: O(1) when item is at the first position
                    worst: O(N) where N is the length of list
        '''
        node = self.head
        # when item is at the last positon, loop runs n times
        for i in range(len(self)):
            if node.item == item:
                return True
            else:
                node = node.next
        return False

    def __getitem__(self, index):
        '''
        function retrieves item from the list at position index
        precondition: list is not empty
        :param: index: position input from the user
        postcondition:
        :return: item at position index of the list
        complexity: best: O(1) when index is 0
                    worst: O(N) where N is the length of list
        '''
        if index >= len(self) or index < -len(self):
            raise IndexError

        if index == 0:
            return self.head.item
        elif index > 0:
            node = self._get_node(index)
            return node.item
        else:
            # when index is -1, _get_index function is called and ran n times
            node = self._get_node(index + len(self))
            return node.item

    def __setitem__(self, index, item):
        '''
        function replaces item at position index of the list
        precondition:
        :param: index: position input from the user
                item: the item the user want to replace with
        postcondition: item at position index of the list is overwritten
        :return:
        complexity: best: O(1) when index is 0
                    worst: O(N) where N is the length of list
        '''
        if index >= len(self) or index < -len(self):
            raise IndexError

        if index == 0:
            self.head.item = item
        elif index > 0:
            node = self._get_node(index)
            node.item = item
        else:
            # when index is -1, _get_index function is called and ran n times
            node = self._get_node(index + len(self))
            node.item = item

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
            node = self.head
            for i in range(len(self)):
                if node.item != other[i]:
                    return False
                node = node.next
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
        return ListIterator(self.head)

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

    def is_full(self):
        '''
        function checks if the array is full
        precondition:
        :param:
        postcondition:
        :return: boolean value: False if array has space
        complexity: best and worst: O(1)
        '''
        return False

    def _get_node(self, index):
        '''
        function gets the address of the node at position index of the list
        precondition:
        :param: index: position input from the user
        postcondition:
        :return: address of the node
        complexity: best: O(1) when index is 1
                    worst: O(N) where N is the length of list and index is -1
        '''
        assert 0 <= index < len(self), 'Index out of bounds.'
        node = self.head
        # when index is -1, loop runs n times
        for i in range(index):
            node = node.next
        return node

    def append(self, item):
        '''
        function appends item into array
        precondition:
        :param: item: the item the user wants to append into the array
        postcondition: array space decreases by one
        :return:
        complexity: best and worst: O(N) where N is the length of list
        '''
        if self.head is not None:
            # when list is not empty, _get_index function is called and ran n times
            node = self._get_node(len(self) - 1)
            node.next = Node(item, node.next)
        else:
            self.head = Node(item, None)
        self.count += 1

    def insert(self, index, item):
        '''
        function inserts item into list at position index
        precondition:
        :param: index: position input from the user
                item: the item the user wants to insert into the list
        postcondition: array space decreases by one
        :return:
        complexity: best: O(1) when the index is 0
                    worst: O(N) where N is the length of list and index is -1
        '''
        if index >= len(self) or index < -len(self):
            raise IndexError

        if not self.is_full():
            if index == 0:
                self.head = Node(item, self.head)
            elif index > 0:
                node = self._get_node(index - 1)
                node.next = Node(item, node.next)
            else:
                # when index is -1, _get_index function is called and ran n times
                if index + len(self) == 0:
                    self.head = Node(item, self.head)
                node = self._get_node(index + len(self) - 1)
                node.next = Node(item, node.next)
            self.count += 1

    def remove(self, item):
        '''
        function removes item from the list
        precondition: list is not empty
        :param: item: the item the user wants to remove from the list
        postcondition: array space increases by one
        :return:
        complexity: best: O(1) when item is at the first position
                    worst: O(N) where N is the length of list
        '''
        if item not in self:
            raise ValueError

        node = self.head
        # when item is at first position, loop runs 1 time
        # when item is at the last position, loop runs n times
        for i in range(len(self)):
            if node.item == item:
                break
            node = node.next

        if node == self.head:
            self.head = node.next
        else:
            # when item is at the last position, _get_index function is called and ran n times
            node = self._get_node(i - 1)
            node.next = node.next.next
        self.count -= 1

    def delete(self, index):
        '''
        function deletes item from list at position index
        precondition:
        :param: index: position input from the user
        postcondition: array space increases by one
        :return:
        complexity: best: O(1) when index is 0
                    worst: O(N) where N is the length of list and index is -1
        '''
        if index >= len(self) or index < -len(self):
            raise IndexError

        if index == 0:
            self.head = self.head.next
        elif index > 0:
            node = self._get_node(index - 1)
            node.next = node.next.next
        else:
            # when index is -1, _get_index function is called and ran n times
            node = self._get_node(index + len(self) - 1)
            node.next = node.next.next
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
                    if self[j] < self[min]:
                        min = j
                temp = self[i]
                self[i] = self[min]
                self[min] = temp

        elif reverse == True:
            # when list is sorted, both first and second loop still runs n times
            for i in range(len(self)):
                max = i
                for j in range(i + 1, len(self)):
                    if self[j] > self[max]:
                        max = j
                temp = self[i]
                self[i] = self[max]
                self[max] = temp


if __name__ == '__main__':
    while True:
        try:
            array = LinkedList()
            break
        except ValueError:
            print('Enter numbers only.')
        except AssertionError as e:
            print(e)

        my_table = LinkedList()
        my_table[0] = "Eva"
        my_table[0] = "Amy"
        my_table[0] = "Tim"
        my_table[0] = "Ron"
        my_table[0] = "Jan"
        print(my_table)