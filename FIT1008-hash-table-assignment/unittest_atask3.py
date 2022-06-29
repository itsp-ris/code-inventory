import unittest
from atask3 import HashTableLinear as HashTable


class TestHashTable(unittest.TestCase):
    def test_setitem(self):
        table = HashTable(10, 3)
        table["Eva"] = "Eva"
        table["Amy"] = "Amy"
        table["Tim"] = "Tim"
        table["Ron"] = "Ron"
        table["Jan"] = "Jan"
        HashTable.__setitem__(table, 'Ben', 'Ben')
        self.assertEqual(str(table), '(Tim, Tim)\n(Ron, Ron)\n(Eva, Eva)\n(Amy, Amy)\n(Jan, Jan)\n(Ben, Ben)\n')
        self.assertEqual(table.collision, 0)

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
        self.assertEqual(table.collision, 3)
        with self.assertRaises(Exception):
            HashTable.__setitem__(table, 'Ben', 'Ben')

    def test_trackload(self):
        table = HashTable(10, 3)
        table["Eva"] = "Eva"
        table["Amy"] = "Amy"
        table["Tim"] = "Tim"
        table["Ron"] = "Ron"
        table["Jan"] = "Jan"
        self.assertEqual(HashTable.track_load(table), 0.5)

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
        self.assertEqual(HashTable.track_load(table), 1.0)

        table = HashTable(10, 3)
        self.assertEqual(HashTable.track_load(table), 0)

    def test_trackavgprobelength(self):
        table = HashTable(10, 3)
        table["Eva"] = "Eva"
        table["Amy"] = "Amy"
        table["Tim"] = "Tim"
        table["Ron"] = "Ron"
        table["Jan"] = "Jan"
        self.assertEqual(HashTable.track_avg_probe_length(table), 0)

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
        self.assertEqual(HashTable.track_avg_probe_length(table), 1.8)

        table = HashTable(10, 3)
        with self.assertRaises(AssertionError):
            HashTable.track_avg_probe_length(table)


if __name__ == '__main__':
    unittest.main()

