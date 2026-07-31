#!/usr/bin/python3
"""Module that defines the Square class with a custom string repr."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class that represents a square, inherits from Rectangle."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): the size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Return the square description as [Square] width/height."""
        return "[Square] {}/{}".format(
            self._Rectangle__width, self._Rectangle__height)
