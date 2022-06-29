import unittest
from task4 import opening
from task2 import Array
from task3 import LinkedList as Array

class Test_Function(unittest.TestCase):
    def test_opening(self):
        file = opening('test')
        file_list = Array()
        for i in range(len(file)):
            file_list.append(file[i])
        self.assertEqual(str(file_list), "5 seconds to summer\nLol you\n33 aha'h\n291 lol\nHello@@@\n31\nyou rock\nstink hell\n")

        file = opening('test2')
        file_list = Array()
        for i in range(len(file)):
            file_list.append(file[i])
        self.assertEqual(str(file_list), 'hi' + '\n' + '\n' + 'lol' + '\n')
        
        file = opening('test3')
        file_list = Array()
        for i in range(len(file)):
            file_list.append(file[i])
        self.assertEqual(str(file_list),'\n')

if __name__=='__main__':
    unittest.main()
        
