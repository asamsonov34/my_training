# Функция, где на ноль делить можно (возвращает бесконечность)
from math import inf

def divide(a, b):
    if b == 0:
        return inf
    else:
        return a / b