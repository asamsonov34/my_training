my_str = input('Введите текст: ')
# my_str = 'My House Is Great!' # for easier debugging
print('Символов во введённом тексте: ', len(my_str), sep='')
print('Ваш текст в верхнем регистре: «', my_str.upper(), '»', sep='')
print('Ваш текст в нижнем регистре: «', my_str.lower(), '»', sep='')
print('Ваш текст без пробелов: «', my_str.replace(' ', ''),
'», он стал короче на ',
str(len(my_str)-len(my_str.replace(' ', ''))),
' символ(а/ов)', sep='')
print('Ваш текст начинается с «', my_str[0], '» и заканчивается на «', my_str[-1], '»', sep='')