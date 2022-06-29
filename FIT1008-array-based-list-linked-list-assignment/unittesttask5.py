import unittest
from task5 import Editor

class Test_Editor(unittest.TestCase):
    def test_insert_num(self):
        list = Editor()
        with self.assertRaises(AssertionError):
            Editor.insert_num(list, 0, 'abc')

        list = Editor()
        Editor.read_filename(list, 'test')
        with self.assertRaises(IndexError):
            Editor.insert_num(list, 10, 'abc')

        list = Editor()
        Editor.read_filename(list, 'test')
        Editor.insert_num(list, 1, 'abc')
        self.assertEqual(list.array, ['abc', '5 seconds to summer', 'Lol you', "33 aha'h", '291 lol', 'Hello@@@', '31', 'you rock', 'stink hell'])

        list = Editor()
        Editor.read_filename(list, 'test')
        Editor.insert_num(list, -1, 'abc')
        self.assertEqual(list.array, ['5 seconds to summer', 'Lol you', "33 aha'h", '291 lol', 'Hello@@@', '31', 'you rock', 'abc', 'stink hell'])

    def test_delete_num(self):
        list = Editor()
        with self.assertRaises(AssertionError):
            Editor.delete_num(list, 0)

        list = Editor()
        Editor.read_filename(list, 'test')
        with self.assertRaises(IndexError):
            Editor.delete_num(list, 10)

        list = Editor()
        Editor.read_filename(list, 'test')
        Editor.delete_num(list, 1)
        self.assertEqual(str(list.array), "Lol you\n33 aha'h\n291 lol\nHello@@@\n31\nyou rock\nstink hell\n")

        list = Editor()
        Editor.read_filename(list, 'test')
        Editor.delete_num(list, -1)
        self.assertEqual(str(list.array), "5 seconds to summer\nLol you\n33 aha'h\n291 lol\nHello@@@\n31\nyou rock\n")

        list = Editor()
        Editor.read_filename(list, 'test')
        Editor.delete_num(list)
        self.assertEqual(str(list.array), '')

    def test_read_filename(self):
        with self.assertRaises(Exception):
            Editor.read_filename('something')

        other = ['5 seconds to summer', 'Lol you', "33 aha'h", '291 lol', 'Hello@@@', '31', 'you rock', 'stink hell']
        list = Editor()
        Editor.read_filename(list, 'test')
        self.assertEqual(list.array, other)

    def test_write_filename(self):
        list = Editor()
        Editor.read_filename(list, 'test')
        Editor.write_filename(list, 'done')
        other = Editor()
        Editor.read_filename(other, 'done')
        self.assertEqual(str(list.array), str(other.array))

        list = Editor()
        Editor.read_filename(list, 'test')
        Editor.write_filename(list, 'done')
        Editor.write_filename(list, 'done')
        other = Editor()
        Editor.read_filename(other, 'done')
        self.assertEqual(str(list.array), str(other.array))

    def test_search_word(self):
        list = Editor()
        with self.assertRaises(AssertionError):
            Editor.search_word(list, 'lol')

        list = Editor()
        Editor.read_filename(list, 'test')
        self.assertEqual(Editor.search_word(list, 'lol'), '2\n4\n')

        list = Editor()
        Editor.read_filename(list, 'test')
        self.assertEqual(Editor.search_word(list, 'bye'), 'Not Found')

        list = Editor()
        Editor.read_filename(list, 'test')
        self.assertEqual(Editor.search_word(list, 'Lol'), '2\n4\n')

    def test_print_num1_num2(self):
        list = Editor()
        Editor.read_filename(list, 'test')
        self.assertEqual(Editor.print_num1_num2(list, 1, 3), "5 seconds to summer\nLol you\n33 aha'h\n")

        list = Editor()
        Editor.read_filename(list, 'test')
        self.assertEqual(Editor.print_num1_num2(list), "5 seconds to summer\nLol you\n33 aha'h\n291 lol\nHello@@@\n31\nyou rock\nstink hell\n")

        list = Editor()
        Editor.read_filename(list, 'test')
        with self.assertRaises(AssertionError):
            Editor.print_num1_num2(list, 3, 1)

        list = Editor()
        Editor.read_filename(list, 'test')
        with self.assertRaises(IndexError):
            Editor.print_num1_num2(list, 1, 11)


if __name__ == '__main__':
    unittest.main()
