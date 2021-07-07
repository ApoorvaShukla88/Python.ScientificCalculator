import unittest
from calculator import Basic, Intermediate


class TestStringMethods(unittest.TestCase):

    def test_add(self):
        self.assertEqual(Basic.add(3, 3), 6)

    def test_add2(self):

        self.assertEqual(Basic.a(12, -10), 2)

    def test_add3(self):
        Basic()
        self.assertEqual(Basic.a(5, 8), 13)

    def test_sub(self):
        Basic()
        self.assertEqual(Basic.s(9, 3), 6)

    def test_sub(self):
        Basic = Basic()
        self.assertEqual(Basic.s(9, 3), 6)


if __name__ == '__main__':
    unittest.main()
