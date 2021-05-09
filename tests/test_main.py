import unittest
import snoop

from basic.main import fizzbuzz, ops, loops, make_calls


class MyTestCase(unittest.TestCase):

    @snoop(depth=float('inf'))
    def test_fizzbuzz(self):
        s = fizzbuzz(100)
        self.assertEqual(s, 68)

    @snoop(depth=float('inf'))
    def test_ops(self):
        s = ops(100, 10)
        self.assertEqual(s, 90)

    @snoop(depth=float('inf'))
    def test_loops(self):
        s = loops()
        self.assertEqual(s, 9)

    @snoop(depth=float('inf'))
    def test_calls(self):
        s = make_calls()
        self.assertEqual(s, None)


if __name__ == '__main__':
    unittest.main()
