import unittest
from atask5 import HashTableSeparateChaining as HashTable


class TestHashTable(unittest.TestCase):
    def test_str(self):
        table = HashTable(10, 3)
        table["Eva"] = "Eva"
        table["Amy"] = "Amy"
        table["Tim"] = "Tim"
        table["Ron"] = "Ron"
        table["Jan"] = "Jan"
        self.assertEqual(str(table), '(Tim, Tim)\n(Ron, Ron)\n(Eva, Eva)\n(Amy, Amy)\n(Jan, Jan)\n')

        table = HashTable(10, 3)
        self.assertEqual(str(table), '')

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
        table["Kim"] = "Kim"
        table["Dot"] = "Dot"
        table["Ann"] = "Ann"
        table["Jim"] = "Jim"
        table["Jon"] = "Jon"
        table["Amm"] = "Amm"
        table["Pij"] = "Pij"
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
        self.assertEqual(table.collision, 1)

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
        self.assertEqual(str(table), '(Tim, Tim)\n(Jim, Jim)\n(Ron, Ron)\n(Dot, Dot)\n(Amm, Amm)\n(Pij, Pij)\n(Eva, '
                                     'Eva)\n(Amy, Amy)\n(Ann, Ann)\n(Jan, Jan)\n(Ben, Ben)\n(Kim, Kim)\n(Jon, Jon)\n')
        self.assertEqual(table.collision, 6)


if __name__ == '__main__':
    unittest.main()
