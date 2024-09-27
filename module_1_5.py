immutable_var = 10, 20, 30, 40, 50, 'чемодан'
print('Создан кортеж', immutable_var)

# просто попробовать цикл со счётчиком в Питоне
# и перебрать в нём кортеж по индексам:
print("Кортеж immutable_var состоит из следующих членов:")
for i in range(len(immutable_var)):
    print(immutable_var[i])
# Попытаемся изменить "чемодан" на "крокодил":
try:
    immutable_var[5] = "крокодил"
except TypeError:
    # В задании требуется объяснить, почему низя:
    print("Ошибка: тип коллекции «Кортеж» не поддерживает изменение её членов.")

mutable_list = [10, 20, 30, 40, 50, 60, "чемодан"]
print('Создан список', mutable_list)

for i in range(len(mutable_list)-1):
    mutable_list[i] = int(mutable_list[i] / 2)
mutable_list[len(mutable_list)-1] = 'крокодил' # просто посмотреть, как именно работает len()
print('Список с изменёнными элементами:', mutable_list)

# Попробуем немного посложнее — с проверкой типа данных каждого члена списка
# (int, str или любой другой).
# Добавим, например, логический тип:
mutable_list.append(True)
# ... а потом изменим члены списка в соответствии с их типом:
for i in range(len(mutable_list)):
    if type(mutable_list[i]) == int:
        mutable_list[i] = mutable_list[i] * 10
    elif type(mutable_list[i]) == str:
        mutable_list[i] = mutable_list[i][::-1]
    else:
        mutable_list[i] = str(mutable_list[i]) + " — чозаботва?"
print('Список с ещё более изменёнными элементами:', mutable_list)


# print(type(mutable_list[1]) == int)