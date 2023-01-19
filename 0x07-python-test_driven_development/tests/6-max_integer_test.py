#!/usr/bin/python3
import unittest
from 6-max_integer import max_integer

class Testmax_integer(unittest.TestCase):
    def test_max_integer(self):
        """tests normal list of ints
        """

        example = max_integer([1, 2, 3,4])
        self.assertEqual(example, 4)

    def test_max_integer_empty(self):
        """ tests if list is empty
        """

        example = max_integer([])
        self.assertEqual(example, None)

    def test_max_integer_neg:
        """ tests if list has a negative int
        """

        example = max_integer([-1, -2, -3, -4])
        self.assertEqual(example, -1)

    def test_max_integer_one_input:
        """ tests if list has only one item
        """

        example = max_integer([-1])
        self.assertEqual(example, -1)

    def test_max_integer_float(self):
        example = max_integer([1.53, 15.5, -9, 15, 6])
        self.assertEqual(example, 15.5)
