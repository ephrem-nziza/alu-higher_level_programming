#!/usr/bin/python3
"""Module that defines the Student class with save/reload support."""


class Student:
    """Represents a student with a first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): the student's first name.
            last_name (str): the student's last name.
            age (int): the student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of this Student instance.

        Args:
            attrs (list): optional list of attribute names to keep.
                When it is not a list of strings, every attribute is
                included instead.

        Returns:
            dict: the filtered or full attribute dictionary.
        """
        if isinstance(attrs, list) and all(
                isinstance(attr, str) for attr in attrs):
            return {
                key: value for key, value in self.__dict__.items()
                if key in attrs
            }
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of this Student from a dictionary.

        Args:
            json (dict): a mapping of attribute names to new values.
        """
        for key, value in json.items():
            setattr(self, key, value)
