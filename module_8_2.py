def  personal_sum(numbers):
    result = 0
    incorrect_data = 0
    # Здесь пробуем вложенность try-ев:
    try:
        for i in range(len(numbers)):
            try:
                result += numbers[i]
            except TypeError:
                incorrect_data += 1
                print(f'Некорректный тип данных для подсчёта суммы: {numbers[i]}')
    except TypeError:
        print(f'В <numbers> записан некорректный тип данных — {type(numbers)}, а не коллекция')
    return (result, incorrect_data)


def calculate_average(numbers):
    result = None
    # А здесь плоский try с двумя except-ами:
    try:
        personal_sum_data = personal_sum(numbers) # Если не писать в переменную, а в подсчёте использовать
                                                  # personal_sum[0|1], всё работает, но строки, где в этимологии
                                                  # есть исключения, двоятся. т. к. ф-ция вызывается дважды.
        result = personal_sum_data[0] / (len(numbers) - personal_sum_data[1]) # Считать только числа
    except ZeroDivisionError:
        result = 0
    except TypeError:
        pass
    return result

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([])}') # Передана пустая коллекция
print(f'Результат 5: {calculate_average([42, 15, 36, 13])}') # Всё должно работать