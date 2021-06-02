import numpy

def Leibniz():
    denomenator, sum, numerator = 1, 0, 1
    num = 1.00
    while round(sum, 2) != round(numpy.pi / 4, 2):
        if denomenator != 0:
            num = round(numerator / denomenator, 4)
        sum += num
        denomenator += 2
        numerator *= -1
        yield num


for number in Leibniz():
    print(number)