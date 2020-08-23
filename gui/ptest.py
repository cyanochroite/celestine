# coding=utf-8
import unittest
from mem_dixy.tag.alphabet import logical


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        print("hi")
        #self.widget = Widget('The widget')

    def tearDown(self):
        print("bye")
        # self.widget.dispose()

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


class MoreMonkey(unittest.TestCase):

    def setUp(self):
        self._set = logical
        self._list = list(logical)

    def tearDown(self):
        print("s")
        # self.widget.dispose()

    def test_upper(self):
        print(self._list)
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()
