# test_rectangle.py
import unittest
from src.rectangle import Rectangle

class TestRectangleCalculator(unittest.TestCase):

    def test_calculate_area(self):
        # Arrange
        width = 5
        height = 3
        expected_area = width * height

        # Act
        rectangle = Rectangle(width, height)
        actual_area = rectangle.calculate_area()

        # Assert
        self.assertEqual(actual_area, expected_area)

    def test_calculate_perimeter(self):
        # Arrange
        width = 5
        height = 3
        expected_perimeter = 2 * (width + height)

        # Act
        rectangle = Rectangle(width, height)
        actual_perimeter = rectangle.calculate_perimeter()

        # Assert
        self.assertEqual(actual_perimeter, expected_perimeter)

if __name__ == '__main__':
    unittest.main()