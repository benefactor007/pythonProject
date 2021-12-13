import math


def area(radius):
    temp = math.pi * radius ** 2
    return temp


def area(radius):
    return math.pi * radius ** 2


def absoluteValue(x):
    if x < 0:
        return -x
    elif x > 0:
        return x


num = raw_input('Write a number: ')

if '.' in num:
    num = float(num)
    print absoluteValue(num)
else:
    numInt = int(num)
    print absoluteValue(num)


