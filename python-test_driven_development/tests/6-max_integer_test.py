#!/usr/bin/python3
"""Holberton School."""
import unittest


max_integer = __import__('6-max_integer').max_integer


class test_max_integer(unittest.TestCase):
    """Test of max_integer function."""

    def test_emptylist(self):
        """Test of max_integer function."""
        list = []
        self.max_integer(list)

    def test_isnegative(self):
        """Test of max_integer function."""
        self.assertTrue(max_integer(list=[-1, -2, -3, -4]), -1)

    def test_isinteger(self):
        """String passed."""
        self.assertTrue(max_integer(list=[1, 90, 2, 13, 34, 5, -13, 3]), 90)

    def test_isinteger2(self):
        """Test with negative values."""
        self.assertTrue(max_integer(list=[9, -1, 2, 3, 4, -30, 2]), 9)

    def test_justone(self):
        """Test with one value."""
        self.assertTrue(max_integer(list=[1]), 1)

    def test_empty(self):
        """Test with empty list."""
        self.assertTrue(max_integer(list=[]), None)


if __name__ == '__main__':
    unittest.main()
