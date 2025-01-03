def add_em_up(a, b):
    result = None
    try:
        result = a + b
    except TypeError: # Если <a> и <b> — разных типов...
        result = str(a) + str(b) # ... то складываем их как строки.
        if isinstance(b, str): # Если <b> — строка — значит, <a> преобразуется в строку...
            print('Успешно сложены 2 строки — первое слагаемое (число) преобразовано в строку.')
        else: # ... # А если <a> — строка — значит, <b> преобразуется в строку.
            print('Успешно сложены 2 строки — второе слагаемое (число) преобразовано в строку.')
    else:
        if isinstance(a, str): # Если <a> — строка, то и <b> — строка...
            print('Успешно сложены 2 строки.')
        else:  # ... а если <a> — число, то и <b> — число.
            print('Успешно сложены 2 числа.')
    finally:
        print('Результат:')
    return result

print('——————————————————————————————————————————————————————————————————————————') # Для лучшей читаемости вывода:
print(add_em_up(10.5, 1))
print('——————————————————————————————————————————————————————————————————————————') # чтобы вывод каждого вызова
print(add_em_up('10.5', '1'))
print('——————————————————————————————————————————————————————————————————————————') # не «слипался» с остальными.
print(add_em_up(10.5, '1'))
print('——————————————————————————————————————————————————————————————————————————')
print(add_em_up('10.5', 1))