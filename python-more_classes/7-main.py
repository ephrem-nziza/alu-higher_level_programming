#!/usr/bin/python3
Rectangle = __import__('7-rectangle').Rectangle

my_rectangle = Rectangle(3, 2)
print(my_rectangle)
print("--")

my_rectangle.print_symbol = "&"
print(my_rectangle)
print("--")

my_rectangle.print_symbol = ["a", "b"]
print(my_rectangle)
