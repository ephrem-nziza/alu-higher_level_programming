#!/usr/bin/python3
Rectangle = __import__('6-rectangle').Rectangle

r1 = Rectangle(10, 2)
print("{} instances".format(Rectangle.number_of_instances))
r2 = Rectangle(2, 10)
print("{} instances".format(Rectangle.number_of_instances))
del r1
print("{} instances".format(Rectangle.number_of_instances))
del r2
print("{} instances".format(Rectangle.number_of_instances))
