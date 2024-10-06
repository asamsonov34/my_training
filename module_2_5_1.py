# Вариант выполнения задачи по функциям с параметром,
# где и внутри строк числа, соответствующие колонкам,
# генерятся рандомно.

import random

def get_mtx(lines, cols, minval, maxval):
    mtx = []
    for i in range(lines):
        line_lst = []
        for j in range(cols):
            line_lst.append(rand_n(minval, maxval))
        mtx.append(line_lst)
    return mtx

def rand_n(min, max):
    return random.randrange(min, max)

print(get_mtx(2, 2, 0, 101))
print(get_mtx(3, 5, 0, 101))
print(get_mtx(4, 2, 0, 101))