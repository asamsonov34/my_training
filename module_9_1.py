# Я, правда, функции не только те использовал, которые в задании... А те, которые те, — не всегда так...
# А началось всё с того, что в задании предлагается назвать переменную int_list ("список ЦЕЛЫХ чисел" — int_ же),
# и тут же # говорится, что это список из чисел (int, float). Ну, раз float — подумал, надо бы дробные
# использовать... и понеслась... типа, а дробные можно округлить... а не сделать ли список генерируемым...
# а что ещё можно с числами сделать... Ну, и уже видео по списковым сборкам посмотрел — надо попробовать...
# В общем, не успел оглянуться, как вот:

from random import randint

nums = [round(x / 10 * randint(-5, 5), 1) for x in range(10, 17)] # Сгенерим и покажем первоначальный список
print(f'Первоначальный список:\n{nums}') # Сепаратор вывода

def apply_all_funcs(lst, *funcs):
    result_dic = {}
    for func in funcs:
        result_dic.update({func.__name__: func(lst)})
    return result_dic

# Удвоим числа из первоначального списка
def dbl_nums(lst):
    return [a * 2 for a in lst]

# Округлим числа в первоначальном списке до целых
def rnd_nums(lst):
    return [int(round(a, 0)) for a in lst]

# Представим числа из первоначального списка в строковом виде
def num2str(lst):
    return [str(a) for a in lst]

# Найдём среднее арифметическое чисел в первоначальном списке (округлим его до 2 цифр после запятой):
def avg_of_nums(lst):
    return round(sum(lst)/len(lst), 2) # Чтоб два раза не вставать — сразу и sum(), и len()

# Найдём наибольшее и наименьшее из чисел первоначального списка
def min_and_max(lst):
    return f'Наименьшее: {min(lst)}, Наибольшее: {max(lst)}' # Тоже чтоб два раза не вставать

# Отсортируем первоначальный список
def sorted(lst):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swapped = True
    return(lst)

print('•••\n', apply_all_funcs(nums, dbl_nums, rnd_nums, avg_of_nums))
print('•••\n', apply_all_funcs(nums, num2str, sorted, min_and_max))
