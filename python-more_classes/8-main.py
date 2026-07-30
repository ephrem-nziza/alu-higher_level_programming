#!/usr/bin/python3
Rectangle = __import__('8-rectangle').Rectangle

r1 = Rectangle(5, 5)
r2 = Rectangle(3, 5)
print(Rectangle.bigger_or_equal(r1, r2))
print(Rectangle.bigger_or_equal(r2, r1))
