import unittest

class testhoge:
    def __init__(self):
        self.foo = 0
        self.hogestr = "hello world"
    def get_foo(self):
        return self.foo
    def get_hoge(self):
        return self.hogestr

class TestStringMethods(unittest.TestCase):
    def test_new(self):
        t = testhoge()
        self.assertEqual("hello world", t.get_hoge())
        self.assertEqual(0, t.get_foo())
        # self.assertEqual(1, t.get_foo())

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

if __name__ == '__main__':
    unittest.main()