#!/usr/bin/python3
Rectangle = __import__('4-rectangle').Rectangle

my_rectangle = Rectangle(3, 2)
print(my_rectangle)
print(repr(my_rectangle))
print(str(my_rectangle))

list_rectangles = [Rectangle(2, 2), Rectangle(4, 6)]
print(list_rectangles)
