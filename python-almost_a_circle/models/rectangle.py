#!/usr/bin/python3
"""Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor."""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter to set the value."""
        self.__width = value

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter."""
        self.__height = value

    @property
    def x(self):
        """Getter for x."""
        return self.__x

    @x.setter
    def x(self, value):
        """X setter."""
        self.__x = value

    @property
    def y(self):
        """Getter for x."""
        return self.__y

    @y.setter
    def y(self, value):
        """Y setter."""
        self.__y = value

    def area(self):
        """Return area of rectangle."""
        return self.__width * self.__heigth

    def display(self):
        """Display #."""
        print("\n" * self.y, end="")
        for i in range(self.height):
            print(self.x * " ", end="")
            print(self.width * "#")

    def __str__(self):
        """Magic method lol."""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y}\
                - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """Update func."""
        for j, kwg in kwargs.items():
            self.id = kwg
            self.width = kwg
            self.heigt = kwg
            self.x = kwg
            self.y = kwg
