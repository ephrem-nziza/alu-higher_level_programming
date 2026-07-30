#!/usr/bin/python3
Rectangle = __import__('2-rectangle').Rectangle

my_rectangle = Rectangle(3, 2)
print(my_rectangle.area())
print(my_rectangle.perimeter())

my_rectangle2 = Rectangle(3, 0)
print(my_rectangle2.area())
print(my_rectangle2.perimeter())
