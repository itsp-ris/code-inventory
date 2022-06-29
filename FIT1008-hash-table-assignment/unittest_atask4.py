import unittest
from atask4 import HashTableQuadratic as HashTable


class TestHashTable(unittest.TestCase):
    def test_getitem(self):
        table = HashTable(10, 3)
        table["Eva"] = "Eva"
        table["Amy"] = "Amy"
        table["Tim"] = "Tim"
        table["Ron"] = "Ron"
        table["Jan"] = "Jan"
        self.assertEqual(table['Eva'], 'Eva')

        table = HashTable(10, 3)
        table["Eva"] = "Eva"
        table["Amy"] = "Amy"
        table["Tim"] = "Tim"
        table["Ron"] = "Ron"
        table["Jan"] = "Jan"
        with self.assertRaises(KeyError):
            HashTable.__getitem__(table, 'Ben')

    def test_setitem(self):
        table = HashTable(10, 3)
        table["Eva"] = "Eva"
        table["Amy"] = "Amy"
        table["Tim"] = "Tim"
        table["Ron"] = "Ron"
        table["Jan"] = "Jan"
        HashTable.__setitem__(table, 'Ben', 'Ben')
        self.assertEqual(str(table), '(Tim, Tim)\n(Ron, Ron)\n(Eva, Eva)\n(Amy, Amy)\n(Jan, Jan)\n(Ben, Ben)\n')

        table = HashTable(10, 3)
        table["Eva"] = "Eva"
        table["Amy"] = "Amy"
        table["Tim"] = "Tim"
        table["Ron"] = "Ron"
        table["Jan"] = "Jan"
        table["Kim"] = "Kim"
        table["Dot"] = "Dot"
        table["Ann"] = "Ann"
        table["Jim"] = "Jim"
        table["Jon"] = "Jon"
        table["Amm"] = "Amm"
        table["Pij"] = "Pij"
        HashTable.__setitem__(table, 'Ben', 'Ben')
        self.assertEqual(str(table), '(Jon, Jon)\n(Eva, Eva)\n(Tim, Tim)\n(Ron, Ron)\n(Kim, Kim)\n(Amy, Amy)\n(Dot, '
                                     'Dot)\n(Amm, Amm)\n(Pij, Pij)\n(Jan, Jan)\n(Ann, Ann)\n(Jim, Jim)\n(Ben, Ben)\n')

    def test_rehash(self):
        table = HashTable(10, 3)
        table["Eva"] = "Eva"
        table["Amy"] = "Amy"
        table["Tim"] = "Tim"
        table["Ron"] = "Ron"
        table["Jan"] = "Jan"
        self.assertEqual(table.table_size, 10)

        table = HashTable(10, 3)
        table["Eva"] = "Eva"
        table["Amy"] = "Amy"
        table["Tim"] = "Tim"
        table["Ron"] = "Ron"
        table["Jan"] = "Jan"
        table["Kim"] = "Kim"
        table["Dot"] = "Dot"
        table["Ann"] = "Ann"
        table["Jim"] = "Jim"
        table["Jon"] = "Jon"
        table["Amm"] = "Amm"
        table["Pij"] = "Pij"
        self.assertEqual(table.table_size, 21)


if __name__ == '__main__':
    unittest.main()