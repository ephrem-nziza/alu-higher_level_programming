#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle

my_rectangle = Rectangle(3, 2)
print(my_rectangle.width, my_rectangle.height)

my_rectangle.width = 10
my_rectangle.height = 5
print(my_rectangle.width, my_rectangle.height)

try:
    my_rectangle.width = "hello"
except Exception as e:
    print("{}: {}".format(type(e).__name__, e))

try:
    my_rectangle.height = -5
except Exception as e:
    print("{}: {}".format(type(e).__name__, e))
