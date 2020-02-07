import unittest

from src.fizzbuzz import FizzBuzz


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(FizzBuzz().fixxBuzz(), "1 2")


if __name__ == '__main__':
    unittest.main()
