def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print('—————————— 1 ——————————') # Как разделитель "секций" в консоли
print_params()
print_params(a = 2)
print_params(b = 'другая_строка', c = False)
print_params(c = False, b = 'другая_строка')
print_params(b = 25)
print_params(c = [1, 2, 3])
print_params(*[1, 2, 3])

print('—————————— 2 ——————————')
values_list = [True, 11.5, 'Gotcha!']
values_dict = {'a': 'Duck', 'b': False, 'c': 256}
print_params(*values_list)
print_params(**values_dict)

print('—————————— 3 ——————————')
values_list_2 = [None, 'duds']
print_params(*values_list_2, 42)
print_params(42, *values_list_2)