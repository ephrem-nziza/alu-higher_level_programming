#!/usr/bin/python3
Square = __import__('4-square').Square

my_square = Square(5)
print(my_square.area())
my_square.size = 3
print(my_square.area())

try:
    my_square.size = "hello"
except Exception as e:
    print("{}: {}".format(type(e).__name__, e))

try:
    my_square.size = -1
except Exception as e:
    print("{}: {}".format(type(e).__name__, e))
