# Сперва составим словарь из пар {число слева — пароль}. Здесь мне удобнее цикл 'for'

pwd_dict = {}
for given in range(3, 21):
    pwd = ''
    for i in range(1, given):
        for j in range(i, given):
            if given % (i + j) == 0 and i != j:
                pwd = pwd + str(i) + str(j)
    pwd_dict.update({given: pwd})

# Теперь используем числа, введённые юзером, чтобы получить из словаря соответствующие им пароли.
# Если юзер, не вводя число, просто нажмёт Enter, программа попрощается и завершится. Здесь мне
# представляется более подходящим цикл 'while'. Ввод проверяем на корректность.

while True:
    given = input('Введите число, появившееся слева' + chr(10) + '(Enter без ввода числа — завершить): ')
    if given == '': # если юзер нажал Enter без ввода числа
        print('Благодарим за использование нашей программы!')
        break
    else:
        try:
            given = int(given)
        except ValueError:
            print('Невозможно: там могут быть только целые числа с 3 до 20.')
            continue
        if given in range(3, 21):
            print('                     ••• Ваш пароль:', pwd_dict.get(given)) # Пробелы выравнивают ввод и вывод
        else:
            print('Невозможно: там могут быть только целые числа с 3 до 20.')
            continue