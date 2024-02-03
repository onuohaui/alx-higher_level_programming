#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Unittests for the function max_integer(list=[]).
    """

    def test_max_end(self):
        """Test with max at the end."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
    
    def test_max_beginning(self):
        """Test with max at the beginning."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
    
    def test_max_middle(self):
        """Test with max in the middle."""
        self.assertEqual(max_integer([2, 4, 3, 1]), 4)
    
    def test_one_element(self):
        """Test with one element in the list."""
        self.assertEqual(max_integer([4]), 4)
    
    def test_empty_list(self):
        """Test with an empty list."""
        self.assertEqual(max_integer([]), None)

if __name__ == '__main__':
    unittest.main()
