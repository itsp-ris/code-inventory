import unittest
from task2 import Array

class Test_Array(unittest.TestCase):
    def test_str(self):
        array = Array(20)
        for i in range(10):
            Array.append(array, i)
        self.assertEqual(Array.__str__(array), '0' + '\n' + '1' + '\n' + '2' + '\n' + '3' + '\n' + '4' + '\n' + '5' + '\n' + '6' + '\n' + '7' + '\n' + '8' + '\n' + '9' + '\n')

        array = Array(20)
        self.assertEqual(Array.__str__(array), '')

    def test_len(self):
        array = Array(20)
        for i in range(20):
            Array.append(array, i)
        self.assertEqual(Array.__len__(array), 20)

        array = Array(20)
        for i in range(10):
            Array.append(array, i)
        self.assertEqual(Array.__len__(array), 10)

        array = Array(20)
        self.assertEqual(Array.__len__(array), 0)

    def test_contains(self):
        array = Array(20)
        for i in range(10):
            Array.append(array, i)
        self.assertTrue(Array.__contains__(array, 0))

        array = Array(20)
        for i in range(10):
            Array.append(array, i)
        self.assertFalse(Array.__contains__(array, 10))

        array = Array(20)
        self.assertFalse(Array.__contains__(array, 0))

    def test_getitem(self):
        array = Array(20)
        for i in range(10):
            Array.append(array, i)
        self.assertEqual(Array.__getitem__(array, 0), 0)

        array = Array(20)
        for i in range(10):
            Array.append(array, i)
        self.assertEqual(Array.__getitem__(array, -1), 9)

        array = Array(20)
        for i in range(3):
            Array.append(array, i)
        with self.assertRaises(IndexError):
            Array.__getitem__(array, 3)

    def test_setitem(self):
        array = Array(20)
        for i in range(3):
            Array.append(array, i)
        Array.__setitem__(array, 0, 10)
        self.assertEqual(array, [10, 1, 2])

        array = Array(20)
        for i in range(3):
            Array.append(array, i)
        Array.__setitem__(array, -1, 10)
        self.assertEqual(array, [0, 1, 10])

        array = Array(20)
        for i in range(3):
            Array.append(array, i)
        with self.assertRaises(IndexError):
            Array.__setitem__(array, 3, 10)

        array = Array(20)
        with self.assertRaises(AssertionError):
            Array.__setitem__(array, 3, 10)

    def test_eq(self):
        array1 = Array(20)
        for i in range(3):
            Array.append(array1, i)
        array2 = Array(20)
        for i in range(3):
            Array.append(array2, i)
        self.assertTrue(Array.__eq__(array1, array2))

        array1 = Array(20)
        for i in range(3):
            Array.append(array1, i)
        array2 = Array(20)
        for i in range(3):
            Array.append(array2, -i)
        self.assertFalse(Array.__eq__(array1, array2))

        array1 = Array(20)
        for i in range(3):
            Array.append(array1, i)
        array2 = Array(2)
        for i in range(2):
            Array.append(array2, -i)
        self.assertFalse(Array.__eq__(array1, array2))

    def test_iter(self):
        array = Array(3)
        for i in range(3):
            Array.append(array, i)
        the_iter = Array.__iter__(array)
        self.assertEqual(str(next(the_iter)), '0')
        self.assertEqual(str(next(the_iter)), '1')
        self.assertEqual(str(next(the_iter)), '2')
        with self.assertRaises(StopIteration):
            next(the_iter)

    def test_resize(self):
        array = Array(20)
        for  i in range(21):
            Array.append(array, i)
        self.assertEqual(array.size, 40)

        array = Array(40)
        for i in range(20):
            Array.append(array, i)
        for j in range(16):
            Array.delete(array, -1)
        self.assertEqual(array.size, 20)

        array = Array(20)
        for i in range(10):
            Array.append(array, i)
        self.assertEqual(array.size, 20)

    def test_append(self):
        array = Array(20)
        Array.append(array, 10)
        self.assertEqual(array, [10])

        array = Array(20)
        for i in range(3):
            Array.append(array, i)
        self.assertEqual(array, [0, 1, 2])

    def test_insert(self):
        array = Array(20)
        for i in range(2):
            Array.append(array, i)
        Array.insert(array, 0, 10)
        self.assertEqual(array[0], 10)

        array = Array(20)
        for i in range(2):
            Array.append(array, i)
        Array.insert(array, -1, 10)
        self.assertEqual(array[-2], 10)

        array = Array(20)
        for i in range(2):
            Array.append(array, i)
        with self.assertRaises(IndexError):
            Array.insert(array, 2, 10)

        array = Array(20)
        for i in range(20):
            Array.append(array, i)
        with self.assertRaises(AssertionError):
            Array.insert(array, 2, 10)

        array = Array(20)
        with self.assertRaises(AssertionError):
            Array.insert(array, 2, 10)

    def test_remove(self):
        array = Array(20)
        for i in range(3):
            Array.append(array, i)
        self.assertEqual(Array.remove(array, 0), None)

        array = Array(20)
        for i in range(3):
            Array.append(array, i)
        with self.assertRaises(ValueError):
            Array.remove(array, 3)

        array = Array(20)
        with self.assertRaises(ValueError):
            Array.remove(array, 3)

    def test_delete(self):
        array = Array(20)
        for i in range(3):
            Array.append(array, i)
        Array.delete(array, 0)
        self.assertEqual(array, [1, 2])

        array = Array(20)
        for i in range(3):
            Array.append(array, i)
        Array.delete(array, -1)
        self.assertEqual(array, [0, 1])

        array = Array(20)
        for i in range(3):
            Array.append(array, i)
        with self.assertRaises(IndexError):
            Array.delete(array, 3)

        array = Array(20)
        with self.assertRaises(IndexError):
            Array.delete(array, 3)

    def test_sort(self):
        array = Array(20)
        Array.append(array, 10)
        Array.append(array, -1)
        Array.append(array, 0)
        Array.sort(array, False)
        self.assertEqual(array, [-1, 0, 10])

        array = Array(20)
        Array.append(array, 0)
        Array.append(array, -1)
        Array.append(array, 10)
        Array.sort(array, True)
        self.assertEqual(array, [10, 0, -1])

        array = Array(20)
        Array.append(array, -1)
        Array.append(array, 0)
        Array.append(array, 10)
        Array.sort(array, False)
        self.assertEqual(array, [-1, 0, 10])

        array = Array(20)
        Array.append(array, 10)
        Array.append(array, 0)
        Array.append(array, -1)
        Array.sort(array, True)
        self.assertEqual(array, [10, 0, -1])


if __name__ == '__main__':
    unittest.main()
