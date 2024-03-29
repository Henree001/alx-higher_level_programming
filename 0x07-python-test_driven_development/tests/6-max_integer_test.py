#!/usr/bin/python3
"""Unittest for max_integer([..])"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ tests for max_integer"""

    def test_max_integer_end(self):
        """tests normal list of ints
        """

        example = [1, 2, 3,4]
        self.assertEqual(max_integer(example), 4)

    def test_max_integer_empty(self):
        """ tests if list is empty
        """

        example = []
        self.assertEqual(max_integer(example), None)

    def test_max_integer_neg(self):
        """ tests if list has a negative int
        """

        example = [-1, -2, -3, -4]
        self.assertEqual(max_integer(example), -1)

    def test_max_integer_one_input(self):
        """ tests if list has only one item
        """

        example = [-1]
        self.assertEqual(max_integer(example), -1)

    def test_max_integer_float(self):
        example = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(example), 15.5)

    if __name__ == '__main__':
        unittest.main()
