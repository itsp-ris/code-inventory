import unittest
from atask1 import HashTable


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

    def test_len(self):
        table = HashTable(10, 3)
        table["Eva"] = "Eva"
        table["Amy"] = "Amy"
        table["Tim"] = "Tim"
        table["Ron"] = "Ron"
        table["Jan"] = "Jan"
        self.assertEqual(len(table), 5)

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
        self.assertEqual(len(table), 10)

        table = HashTable(10, 3)
        self.assertEqual(len(table), 0)

    def test_contains(self):
        table = HashTable(10, 3)
        table["Eva"] = "Eva"
        table["Amy"] = "Amy"
        table["Tim"] = "Tim"
        table["Ron"] = "Ron"
        table["Jan"] = "Jan"
        self.assertTrue(HashTable.__contains__(table, 'Eva'))

        table = HashTable(10, 3)
        table["Eva"] = "Eva"
        table["Amy"] = "Amy"
        table["Tim"] = "Tim"
        table["Ron"] = "Ron"
        table["Jan"] = "Jan"
        self.assertFalse(HashTable.__contains__(table, 'Ben'))

        table = HashTable(10, 3)
        self.assertFalse(HashTable.__contains__(table, 'Ben'))

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
        with self.assertRaises(Exception):
            HashTable.__setitem__(table, 'Ben', 'Ben')

    def test_hashvalue(self):
        table = HashTable(10, 3)
        self.assertEqual(HashTable.hash_value(table, 'Eva'), 2)


if __name__ == '__main__':
    unittest.main()

