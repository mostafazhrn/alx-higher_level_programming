#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """This is a test for max_integer
    """
    def test_order_lst(self):
        """This is a test for ordered list
        """
        ordered_list = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered_list), 4)

    def test_unordered_lst(self):
        """This is a test for unordered list
        """
        unordered_list = [4, 3, 2, 1]
        self.assertEqual(max_integer(unordered_list), 4)

    def test_empty_lst(self):
        """This is a test for empty list
        """
        empty_list = []
        self.assertEqual(max_integer(empty_list), None)

    def test_one_element(self):
        """This is a test for one element
        """
        one_element = [1]
        self.assertEqual(max_integer(one_element), 1)

    def test_max_at_the_beginning(self):
        """This is a test for max at the beginning
        """
        max_at_the_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_the_beginning), 4)

    def test_int_float(self):
        """This is a test for int and float
        """
        int_float = [1, 2, 3, 4.0]
        self.assertEqual(max_integer(int_float), 4.0)

    def test_float(self):
        """This is a test for float
        """
        float = [1.0, 2.0, 3.0, 4.0]
        self.assertEqual(max_integer(float), 4.0)

    def test_string(self):
        """This is a test for string
        """
        string = ["a", "b", "c", "d"]
        self.assertEqual(max_integer(string), "d")

    def test_empty_string(self):
        """This is a test for empty string
        """
        empty_string = ["", "", "", ""]
        self.assertEqual(max_integer(empty_string), "")

    def test_lst_of_strings(self):
        """This is a test for list of strings
        """
        lst_of_strings = ["a", "b", "c", "d"]
        self.assertEqual(max_integer(lst_of_strings), "d")


if __name__ == '__main__':
    unittest.main()
