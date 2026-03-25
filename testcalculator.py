import unittest

#  Function to test
def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# Unit Tests
class TestCalculator(unittest.TestCase):

    # 🔹 Normal cases
    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(add(-2, -3), -5)

    def test_divide_normal(self):
        self.assertEqual(divide(10, 2), 5)

    # 🔹 Edge cases
    def test_add_zero(self):
        self.assertEqual(add(0, 5), 5)

    def test_divide_decimal(self):
        self.assertAlmostEqual(divide(1, 3), 0.33333, places=5)

    # 🔹 Error cases
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(5, 0)


# Run tests
if __name__ == "__main__":
    unittest.main()