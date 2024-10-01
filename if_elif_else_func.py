# Вариант 3:
# Ввод в консоль и проверка корректности ввода вынесены в функцию.

def my_input(count):
    if count == 0:
        prompt = 'Введите число'
    else:
        prompt = '... и ещё одно число'
    a = input(prompt + ': ')
    while True: # Проверить, число ли ввёл юзер, и заодно преобразовать во float
        try:
            a = a.replace(',', '.')  # А вдруг дробь введут с запятой?
            a = float(a)
            break
        except ValueError:
            a = input('Нет, целое число или десятичную дробь: ')
    return a

while True: # Если на запрос в конце "Ещё раз?" ввести Y — вернёмся сюда.
    first = my_input(0)
    second = my_input(1)
    third = my_input(2)

    # Теперь можно и посравнивать:
    if first == second and first == third:
        print('Все три введённых числа равны между собой.')
    elif first == second or first == third or second == third:
        print('Два из трёх введённых чисел равны между собой.')
    else:
        print('Все три введённых числа — разные.')

    # Повторить или завершить?
    rpt = input('Попробуем ещё раз? Y — да; любой другой символ, или просто Enter — завершить: ')
    if rpt.upper() == 'Н': # Вдруг юзер забыл переключиться на англ. раскладку
        rpt = 'Y'
    if rpt.upper() != 'Y':
        print('Благодарим за использование нашей программы!')
        break