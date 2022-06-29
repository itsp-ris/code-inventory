import unittest
import atask6


class TestHashTable(unittest.TestCase):
    def test_freqCount(self):
        content = atask6.open_file('testcase')
        table = atask6.HashTableQuadratic(10, 3)
        atask6.freq_count(content, table)
        self.assertEqual(str(table), '(, 6)\n(of, 2)\n(march, 1)\n(updated, 1)\n(texts, 1)\n(free, 1)\n(arthur, 1)\n'
                                     '(sherlock, 1)\n(1661, 1)\n(date, 1)\n(12, 1)\n(to, 1)\n(electronic, 1)\n'
                                     '(edition, 1)\n(29, 1)\n(release, 1)\n(holmes, 1)\n(title, 1)\n(adventures, 1)\n'
                                     '(most, 1)\n(conan, 1)\n(november, 1)\n(vanilla, 1)\n(plain, 1)\n(1999, 1)\n'
                                     '(the, 2)\n(author, 1)\n(2002, 1)\n(sir, 1)\n(recently, 1)\n(world, 1)\n'
                                     '(welcome, 1)\n(doyle, 1)\n(ebook, 1)\n')

    def test_ranking(self):
        content = atask6.open_file('testcase')
        table = atask6.HashTableQuadratic(10, 3)
        atask6.freq_count(content, table)
        atask6.ranking(table)
        self.assertEqual(str(table), '(, common)\n(of, common)\n(march, common)\n(updated, common)\n(texts, common)\n'
                                     '(free, common)\n(arthur, common)\n(sherlock, common)\n(1661, common)\n'
                                     '(date, common)\n(12, common)\n(to, common)\n(electronic, common)\n'
                                     '(edition, common)\n(29, common)\n(release, common)\n(holmes, common)\n'
                                     '(title, common)\n(adventures, common)\n(most, common)\n(conan, common)\n'
                                     '(november, common)\n(vanilla, common)\n(plain, common)\n(1999, common)\n'
                                     '(the, common)\n(author, common)\n(2002, common)\n(sir, common)\n'
                                     '(recently, common)\n(world, common)\n(welcome, common)\n(doyle, common)\n'
                                     '(ebook, common)\n')


if __name__ == '__main__':
    unittest.main()