#!/usr/bin/python3
"""Holberton School."""


class Rectangle:
    """Class that prints a Rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize Function."""
        type(self).number_of_instances += 1
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        elif self.width == 0 or self.height == 0:
            return ""
        else:
            self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        # elif self.width == 0 or self.height == 0:
        # return ""
        else:
            self.__height = value

    def area(self):
        """Get the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Get the perimeter of the rectangle."""
        # if self.width == 0 or self.height == 0:
        # return 0
        return (2 * (self.width + self.height))

    def __str__(self):
        """Print a hash."""
        if self.width == 0 or self.height == 0:
            return ""
        else:
            rectangle = []
            for i in range(self.height):
                rectangle.append(str(self.print_symbol) * self.width)
            return "\n".join(rectangle)

    def __repr__(self):
        """Repr method."""
        return (f"Rectangle{self.width, self.height}")

    def __del__(self):
        """Delete an instance of the rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Retrieve biggest rectangle based on area."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            area1 = rect_1.area()
            area2 = rect_2.area()
            if area1 == area2:
                return rect_1
            elif area2 > area1:
                return rect_2
            else:
                return rect_1

    @classmethod
    def square(cls, size=0):
        """Square is a rectangle."""
        return Rectangle(size, size)
