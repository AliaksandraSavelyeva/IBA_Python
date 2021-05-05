# 1. Реализуйте рекурсивную функцию нарезания прямоугольника с заданными пользователем сторонами a и b
# на квадраты с наибольшей возможной на каждом этапе стороной.
# Выведите длины ребер получаемых квадратов и кол-во полученных квадратов.

import math

width = int(input('Введите ширину прямоугольника:\n'))
height = int(input('Введите длину прямоугольника:\n'))

def getSquares(a, b):
    if b == 0:
        return 0
    else:
        if a < b:
            temp = a
            a = b
            b = temp
        print("Длина ребра: " + str(b))
        print("Количество квадратов: " + str(math.floor(a / b)))
        return getSquares(b, a % b)

getSquares(width, height)