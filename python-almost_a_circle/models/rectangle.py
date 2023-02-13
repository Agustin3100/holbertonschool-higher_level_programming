#!/usr/bin/python3
"""Holberton School."""


from models.base import Base


class Rectangle(Base):
    """Class for example."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Init func."""
        if type(height) != int:
            raise TypeError("height must be an integer")
        elif type(width) != int:
            raise TypeError("width must be an integer")
        elif type(x) != int:
            raise TypeError("x must be an integer")
        elif type(y) != int:
            raise TypeError("y must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        elif width <= 0:
            raise ValueError("width must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y
            self.width = width
            self.height = height
            self.__x = x
        super().__init__(id)

    @property
    def width(self):
        """Class func."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Class func."""
        return self.__heigth

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__heigth = value

    @property
    def x(self):
        """Class func."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Class func."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return area of rectangle."""
        return self.__width * self.__heigth
