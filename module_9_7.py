def is_prime(func):
    def is_prm(*args):
        res = func(*args)
        if res < 2: # 0 и 1 не являются простыми
            y = False
        elif res % 2 == 0: # Проверим на чётность...
            y = res == 2   # ... а если чётное — не двойка ли это.
        else:
            dvr = 3 # Теперь можно проверять только нечётные делители, начиная с 3.
            while dvr ** 2 <= res and res % dvr != 0: # Если до корня из числа не нашлось делителей — оно простое.
                dvr += 2
            y = dvr ** 2 > res # Как только превысило — дальше можно не перебирать.
        if y:
            say = 'Полученная сумма — ПРОСТОЕ число:   '
        else:
            say = 'Полученная сумма — НЕ ПРОСТОЕ число:'
        return f'{say} {res}' # Мне кажется, так удобнее читать — в одной строчке, а не в двух.
    return is_prm

@is_prime
def sum_three(a, b, c):
    return a + b + c

# Проверка до a + b + c = 75 — дальше, думаю, не стоит,
# да и первые результаты в консоли обрезаются при больших суммах.
for first in range(0, 26):
    for second in range(0, 26):
        for third in range(0, 26):
            print(sum_three(first, second, third))





