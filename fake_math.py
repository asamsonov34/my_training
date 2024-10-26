# Функция, где на ноль делить нельзя
def divide(a, b):
    if b == 0:
        return 'Ошибка: деление на ноль'
    else:
        return a / b