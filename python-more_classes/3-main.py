#!/usr/bin/python3
Rectangle = __import__('3-rectangle').Rectangle

my_rectangle = Rectangle(3, 2)
print(my_rectangle)
print("--")
my_rectangle.width = 5
my_rectangle.height = 4
print(my_rectangle)
