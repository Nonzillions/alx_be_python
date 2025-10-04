import unittest

# Import the buggy function
def square(number):
    # BUG: Incorrect logic, should be number * number
    return number + number

class TestSquareFunction(unittest.TestCase):

    def test_positive_number(self):
        """Test square of a positive number"""
        self.assertEqual(square(3), 9)  # Expected: 9

    def test_negative_number(self):
        """Test square of a negative number"""
        self.assertEqual(square(-4), 16)  # Expected: 16

    def test_zero(self):
        """Test square of zero"""
        self.assertEqual(square(0), 0)  # Expected: 0

    def test_non_integer_input(self):
        """Test square of invalid input type"""
        with self.assertRaises(TypeError):
            square("a")  # Should raise TypeError

if __name__ == "__main__":
    unittest.main()
