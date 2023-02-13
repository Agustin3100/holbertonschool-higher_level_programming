#!/usr/bin/python3
"""Holberton School."""


from models.base import Base


class Rectangle(Base):
    """Class for example."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Init func."""
        self.__width = width
        self.__heigth = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Class func."""
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        """Class func."""
        return self.__heigth

    @height.setter
    def height(self, value):
        self.__heigth = value

    @property
    def x(self):
        """Class func."""
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """Class func."""
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
