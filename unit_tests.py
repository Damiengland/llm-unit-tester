import unittest

# Define the function at the top of the file
def calculate_average(numbers: list[float]) -> float:
    """
    Calculates the average of a list of numbers.

    Args:
        numbers: A list of numbers (integers or floats).

    Returns:
        The average of the numbers.

    Raises:
        ValueError: If the input list is empty.
    """
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    return sum(numbers) / len(numbers)

class TestCalculateAverage(unittest.TestCase):

    def test_average_of_integers(self):
        numbers = [10, 20, 30]
        result = calculate_average(numbers)
        self.assertEqual(result, 20.0, "The average of [10, 20, 30] should be 20.0")

    def test_average_of_floats(self):
        numbers = [10.5, 20.5, 30.5]
        result = calculate_average(numbers)
        self.assertAlmostEqual(result, 20.5, places=1, msg="The average of [10.5, 20.5, 30.5] should be 20.5")

    def test_average_of_mixed_numbers(self):
        numbers = [1, 2.5, 3]
        result = calculate_average(numbers)
        self.assertAlmostEqual(result, 2.1666666666666665, places=7, msg="The average of [1, 2.5, 3] should be 2.1666666666666665")

    def test_average_of_empty_list(self):
        with self.assertRaises(ValueError, msg="An empty list should raise a ValueError"):
            calculate_average([])

    def test_single_element_list(self):
        numbers = [5]
        result = calculate_average(numbers)
        self.assertEqual(result, 5.0, "The average of [5] should be 5.0")

    def test_average_of_negative_numbers(self):
        numbers = [-10, -20, -30]
        result = calculate_average(numbers)
        self.assertEqual(result, -20.0, "The average of [-10, -20, -30] should be -20.0")

if __name__ == '__main__':
    unittest.main()

