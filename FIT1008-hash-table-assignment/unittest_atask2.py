import unittest
import atask2


class TestHashTable(unittest.TestCase):
    def test_openFile(self):
        content = atask2.open_file('testcase')
        self.assertEqual(content, ['**Welcome To The World of Free Plain Vanilla Electronic Texts**', '',
                               'Title: The Adventures of Sherlock Holmes', '', 'Author: Sir Arthur Conan Doyle', '',
                               'Release Date: March, 1999  [EBook #1661]', '[Most recently updated: November 29, 2002]',
                               '', 'Edition: 12'])

    def test_timeInserting(self):
        content = atask2.open_file('testcase')

    def test_writeFile(self):
        content = atask2.open_file('testcase')
        table = atask2.HashTable(400000, 101)
        time_taken = atask2.time_inserting(content, table)
        data = str(400000) +', ' + str(time_taken) + ', '



if __name__ == '__main__':
    unittest.main()
