import unittest

from basic.main import fizzbuzz


class MyTestCase(unittest.TestCase):

    def test_fizzbuzz(self):
        s = fizzbuzz(100)
        self.assertEqual(s, 68)


if __name__ == '__main__':
    unittest.main()
