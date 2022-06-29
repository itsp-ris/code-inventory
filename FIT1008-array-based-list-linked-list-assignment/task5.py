'''
ID: 28390121
author: Priscilla Tham
Date: 03.05.2018
'''
from task2 import Array
from task4 import opening

class Editor:
    def __init__(self):
        '''
        function build an empty array
        precondition: file with Array Based List class imported
        :param:
        postcondition:
        :return:
        complexity: best and worst: O(1)
        '''
        self.array = Array()

    def insert_num(self, index, item):
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
        assert len(self.array) != 0, 'Please read in a file first.'
        if index >= 1:
            self.array.insert(index - 1, item)
        else:
            self.array.insert(index, item)

    def delete_num(self, index = None):
        '''
        function deletes item from list at position index
        precondition:
        :param: index: position input from the user
        postcondition: array space increases by one
        :return:
        complexity: best: O(1) when index is -1
                    worst: O(N) where N is the length of list and index is 0
        '''
        assert len(self.array) != 0, 'Please read in a file first.'
        if index is not None:
            if index >= 1:
                self.array.delete(index - 1)
            else:
                self.array.delete(index)
        else:
            for i in range(len(self.array)):
                self.array.delete(-1)

    def read_filename(self, filename):
        '''
        functions opens and reads a file
        precondition: file exist in directory
        :param filename: the file the user wants to open and read
        postcondition: every line in the file is an item appended to the array
        :return:
        complexity: best: O(1) when there is only one line
                    worst: O(N) where N is the number of lines
        '''
        content = opening(filename)
        # when number of lines == 1, loop runs 1 time
        # when number of lines > 1, loop runs n times
        for i in range(len(content)):
            self.array.append(content[i])

    def write_filename(self, filename):
        '''
        functions writes into a file
        precondition:
        :param filename: the file the user wants to write in
        postcondition: every item in the list is a line written in the file which now exist in the directory
        :return:
        complexity: best: O(1) when there is only one line
                    worst: O(N) where N is the number of lines
        '''
        assert len(self.array) != 0, 'Please read in a file first.'
        file = open(filename + '.txt', 'w')
        lines = ''
        if len(self.array) == 1:
            file.write(lines + str(self.array[-1]))
        else:
            # when number or lines > 1, loop runs n-1 times
            for i in range(len(self.array) - 1):
                lines += str(self.array[i]) + '\n'
            file.write(lines + str(self.array[-1]))
        file.close()

    def search_word(self, word):
        '''
        function search the word user input in the list
        precondition:
        :param word: the word the user want to search
        postcondition: punctuations in the list still remains
        :return: number of the line(s) the word exist in or 'Not Found' if word does not exist in the list
        complexity: best: O(N) where N is the length of list
                    worst: O(N**2) where N is the length of list
        '''
        assert len(self.array) != 0, 'Please read in a file first.'
        num = ''
        punctuation = '''`~!@#$%^&*()_+-={}[]|\:;<>?,./'''
        search_word = ''
        for i in word.lower():
            if i not in punctuation:
                search_word += str(i)

        # when word is not in the list, first loop runs n times
        # when word is in the list, both first and second loop run n times
        for j in range(len(self.array)):
            search_line = ''
            if search_word in self.array[j].lower():
                for k in range(len(self.array[j])):
                    if self.array[j][k].lower() not in punctuation:
                        search_line += str(self.array[j][k])

            for m in range(len(search_line.split())):
                if search_word == search_line.lower().split()[m]:
                    num += str(j + 1) + '\n'

        if num == '':
            return 'Not Found'
        else:
            return num

    def print_num1_num2(self, num1 = None, num2 = None):
        '''
        function concatenates items in the list between position num1 and num2 as a string
        precondition:
        :param num1: starting position input from the user
               num2: ending position input from the user
        postcondition: items in the list are all joined with a new line
        :return: a string type
        complexity: best: O(1) when only there's only one line within the range
                    worst: O(N) where N is the length of list
        '''
        assert len(self.array) != 0, 'List is empty because user deleted everything or please read in a file first.'
        if num2 > len(self.array) or num1 < -len(self.array) or num1 < 1:
            raise IndexError

        string = ''
        if num1 and num2 is not None:
            assert num1 < num2, 'Num1 must be less than Num2'
            for i in range(num1 - 1, num2):
                string += str(self.array[i]) + '\n'
        else:
            # when len(list) == n, loop in str function runs n times
            return str(self.array)
        return string

    def quit(self):
        '''
        function exits from the program
        precondition:
        :param:
        postconditon:
        :return:
        complexity: best and worst: O(1)
        '''
        return exit()


if __name__ == '__main__':
    array = Editor()
    while True:
        try:
            command = input('FIT1008_text_editor (for HELP, type "help")>>> ').split()

            if len(command) == 1:
                if command[0] == 'quit':
                    array.quit()

                elif command[0] == 'help':
                    print('============================================')
                    print('"insert num" -- Insert a text at line "num".')
                    print('--------------------------------------------')
                    print('"read filename" -- Read the content of a file named "filename".')
                    print('--------------------------------------------')
                    print('"write filename" -- Save the file into "filename" file.')
                    print('--------------------------------------------')
                    print('"print num1 num2" -- Print the content of the files in between lines "num1" and "num2".')
                    print('If no line numbers are given, the command will print the whole content.')
                    print('--------------------------------------------')
                    print('"delete num" -- Delete the line "num" from the file.')
                    print('If line "num" is not given, the command will delete the whole content.')
                    print('--------------------------------------------')
                    print('"search word" -- It search "word" into the file.')
                    print('If found, it prints the line number(s), otherwise prints "Not Found".')
                    print('--------------------------------------------')
                    print('"quit" -- Quit from the program.')
                    print('============================================')

                elif command[0] == 'print':
                    print(array.print_num1_num2())

                elif command[0] == 'delete':
                    array.delete_num()

                else:
                    print('?')

            elif len(command) == 2:
                if command[0] == 'insert':
                    item = input('Enter text: ')
                    array.insert_num(int(command[1]), item)

                elif command[0] == 'read':
                    array.read_filename(command[1])

                elif command[0] == 'write':
                    array.write_filename(command[1])

                elif command[0] == 'delete':
                    array.delete_num(int(command[1]))

                elif command[0] == 'search':
                    print(array.search_word(command[1]))

                else:
                    print('?')

            elif len(command) == 3:
                if command[0] == 'print':
                    print(array.print_num1_num2(int(command[1]), int(command[2])))
                else:
                    print('?')

            else:
                print('?')

        except IndexError:
            print('Index out of bounds.')
        except AssertionError as e:
            print(e)
        except Exception:
            print('File does not exist.')