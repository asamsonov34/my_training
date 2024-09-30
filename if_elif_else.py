# Вариант 1: для идеального ввода — только целые числа и десятичные дроби,
# при попытке ввести нечисловые символы программа валится в ValueError

# Замена '.' на ',' — чтобы десятичные дроби можно было вводить и с точкой,
# и с запятой.

first = float(input('Введите первое число: ').replace(',', '.'))
second = float(input('Введите второе число: ').replace(',', '.'))
third = float(input('Введите третье число: ').replace(',', '.'))
if first == second and first == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)