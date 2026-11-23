# Level 6 - Topic 3: Testing
# Writing tests to verify your code works correctly

import unittest

# --- The code we want to test ---
def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]

# --- Unit tests using unittest ---
class TestMathFunctions(unittest.TestCase):

    def test_add_positive(self):
        self.assertEqual(add(3, 4), 7)

    def test_add_negative(self):
        self.assertEqual(add(-1, -1), -2)

    def test_add_zero(self):
        self.assertEqual(add(5, 0), 5)

    def test_divide_normal(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_divide_float(self):
        self.assertAlmostEqual(divide(10, 3), 3.333, places=2)

class TestPalindrome(unittest.TestCase):

    def test_simple(self):
        self.assertTrue(is_palindrome("racecar"))

    def test_with_spaces(self):
        self.assertTrue(is_palindrome("race car"))

    def test_case_insensitive(self):
        self.assertTrue(is_palindrome("Madam"))

    def test_not_palindrome(self):
        self.assertFalse(is_palindrome("hello"))

if __name__ == "__main__":
    unittest.main(verbosity=2)
# To run from terminal: python level6_testing.py
# Or: python -m pytest level6_testing.py  (if pytest installed)
