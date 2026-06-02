import math


def square(side):
    return math.ceil(side * side)


size = float(input("Укажите размер стороны квадрата: "))
print(square(size))
