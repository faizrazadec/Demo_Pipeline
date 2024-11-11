# rectangle.py

class Rectangle:
    def __init__(self, width, height):
        """
        Initialize a Rectangle object.

        Args:
            width (float): Width of the rectangle.
            height (float): Height of the rectangle.
        """
        self.width = width
        self.height = height

    def calculate_area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            float: Area of the rectangle.
        """
        return self.width * self.height

    def calculate_perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            float: Perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)