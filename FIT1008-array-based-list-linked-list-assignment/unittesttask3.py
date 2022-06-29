import unittest
from task3 import LinkedList


class Test_LinkedList(unittest.TestCase):
    def test_str(self):
        list = LinkedList()
        for i in range(3):
            LinkedList.append(list, i)
        self.assertEqual(LinkedList.__str__(list), '0' + '\n' + '1' + '\n' + '2' + '\n')

        list = LinkedList()
        self.assertEqual(LinkedList.__str__(list), '')

    def test_len(self):
        list = LinkedList()
        for i in range(3):
            LinkedList.append(list, i)
        self.assertEqual(LinkedList.__len__(list), 3)

        list = LinkedList()
        for i in range(2):
            LinkedList.append(list, i)
        self.assertEqual(LinkedList.__len__(list), 2)

        list = LinkedList()
        self.assertEqual(LinkedList.__len__(list), 0)

    def test_contains(self):
        list = LinkedList()
        for i in range(3):
            LinkedList.append(list, i)
        self.assertEqual(LinkedList.__contains__(list, 0), True)

        list = LinkedList()
        for i in range(3):
            LinkedList.append(list, i)
        self.assertEqual(LinkedList.__contains__(list, 3), False)

        list = LinkedList()
        self.assertEqual(LinkedList.__contains__(list, 0), False)

    def test_getitem(self):
        list = LinkedList()
        for i in range(3):
            LinkedList.append(list, i)
        self.assertEqual(LinkedList.__getitem__(list, 0), 0)

        list = LinkedList()
        for i in range(3):
            LinkedList.append(list, i)
        self.assertEqual(LinkedList.__getitem__(list, -1), 2)

        list = LinkedList()
        for i in range(3):
            LinkedList.append(list, i)
        with self.assertRaises(IndexError):
            LinkedList.__getitem__(list, 3)

    def test_setitem(self):
        list = LinkedList()
        for i in range(3):
            LinkedList.append(list, i)
        LinkedList.__setitem__(list, 0, 10)
        self.assertEqual(list, [10, 1, 2])

        list = LinkedList()
        for i in range(3):
            LinkedList.append(list, i)
        LinkedList.__setitem__(list, -1, 10)
        self.assertEqual(list, [0, 1, 10])

        list = LinkedList()
        for i in range(3):
            LinkedList.append(list, i)
        with self.assertRaises(IndexError):
            LinkedList.__setitem__(list, 3, 10)

    def test_eq(self):
        list1 = LinkedList()
        for i in range(3):
            LinkedList.append(list1, i)
        list2 = LinkedList()
        for i in range(3):
            LinkedList.append(list2, i)
        self.assertEqual(LinkedList.__eq__(list1, list2), True)

        list1 = LinkedList()
        for i in range(3):
            LinkedList.append(list1, i)
        list2 = LinkedList()
        for i in range(3):
            LinkedList.append(list2, -i)
        self.assertEqual(LinkedList.__eq__(list1, list2), False)

        list1 = LinkedList()
        for i in range(3):
            LinkedList.append(list1, i)
        list2 = LinkedList()
        for i in range(2):
            LinkedList.append(list2, -i)
        self.assertEqual(LinkedList.__eq__(list1, list2), False)

    def test_iter(self):
        list = LinkedList()
        for i in range(3):
            LinkedList.append(list, i)
        the_iter = LinkedList.__iter__(list)
        self.assertEqual(str(next(the_iter)), '0')
        self.assertEqual(str(next(the_iter)), '1')
        self.assertEqual(str(next(the_iter)), '2')
        with self.assertRaises(StopIteration):
            next(the_iter)

    def test_append(self):
        list = LinkedList()
        LinkedList.append(list, 10)
        self.assertEqual(list, [10])

        list = LinkedList()
        for i in range(3):
            LinkedList.append(list, i)
        self.assertEqual(list, [0, 1, 2])

    def test_insert(self):
        list = LinkedList()
        for i in range(2):
            LinkedList.append(list, i)
        LinkedList.insert(list, 0, 10)
        self.assertEqual(list[0], 10)

        list = LinkedList()
        for i in range(2):
            LinkedList.append(list, i)
        LinkedList.insert(list, -1, 10)
        self.assertEqual(list[-2], 10)

        list = LinkedList()
        for i in range(3):
            LinkedList.append(list, i)
        with self.assertRaises(IndexError):
            LinkedList.insert(list, 3, 10)

    def test_remove(self):
        list = LinkedList()
        for i in range(3):
            LinkedList.append(list, i)
        self.assertEqual(LinkedList.remove(list, 0), None)

        list = LinkedList()
        for i in range(3):
            LinkedList.append(list, i)
        with self.assertRaises(ValueError):
            LinkedList.remove(list, 3)

        list = LinkedList()
        with self.assertRaises(ValueError):
            LinkedList.remove(list, 3)

    def test_delete(self):
        list = LinkedList()
        for i in range(3):
            LinkedList.append(list, i)
        LinkedList.delete(list, 0)
        self.assertEqual(list, [1, 2])

        list = LinkedList()
        for i in range(3):
            LinkedList.append(list, i)
        LinkedList.delete(list, -1)
        self.assertEqual(list, [0, 1])

        list = LinkedList()
        for i in range(3):
            LinkedList.append(list, i)
        with self.assertRaises(IndexError):
            LinkedList.delete(list, 3)

        list = LinkedList()
        with self.assertRaises(IndexError):
            LinkedList.delete(list, 3)

    def test_sort(self):
        list = LinkedList()
        LinkedList.append(list, 10)
        LinkedList.append(list, -1)
        LinkedList.append(list, 0)
        LinkedList.sort(list, False)
        self.assertEqual(list, [-1, 0, 10])

        list = LinkedList()
        LinkedList.append(list, 0)
        LinkedList.append(list, -1)
        LinkedList.append(list, 10)
        LinkedList.sort(list, True)
        self.assertEqual(list, [10, 0, -1])

        list = LinkedList()
        LinkedList.append(list, -1)
        LinkedList.append(list, 0)
        LinkedList.append(list, 10)
        LinkedList.sort(list, False)
        self.assertEqual(list, [-1, 0, 10])

        list = LinkedList()
        LinkedList.append(list, 10)
        LinkedList.append(list, 0)
        LinkedList.append(list, -1)
        LinkedList.sort(list, True)
        self.assertEqual(list, [10, 0, -1])


if __name__ == '__main__':
    unittest.main()
