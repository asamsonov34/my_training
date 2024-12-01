import os
from os.path import getmtime
import time

tofile = '' # Данные для записи в файл, см. комментарии на строках 17, 18
for root, dirs, files in os.walk('.'):
    for file in files:
        filepath = os.path.join(root, file)
        filesize = os.path.getsize(filepath)
        filetime = time.strftime("%d.%m.%Y %H:%M", time.localtime(getmtime(filepath)))
        parent_dir = os.path.dirname(filepath)
# Вывод в консоль, как в задании (ну, с некоторым наведением красоты... в моём понимании):
        print('——————————————————————————————————————') # разделитель и переносы строк для лучшей читаемости вывода
        print(f'Обнаружен файл: <{file}>.\nПуть: <{filepath}>.\nРазмер: {filesize} байт.\n'
             f'Время изменения: {filetime}.\nРодительский каталог: <{parent_dir}>')

# А хочу сделать ещё вывод в файл. Не Бог весть какая, но дополнительная практика.
# Сперва подготовим данные для записи в файл, аналогично выводу в консоль:
        tofile += (f'\n——————————————————————————————————————\nОбнаружен файл: <{file}>.\nПуть: <{filepath}>.\n'
                  f'Размер: {filesize} байт.\nВремя изменения: {filetime}.\nРодительский каталог: <{parent_dir}>')
# Теперь пишем подготовленные данные в файл:
file = open('files&paths.txt', 'w', encoding = 'utf-8')
file.write(f'Информация о файлах в каталоге\n<{os.getcwd()}>\nи подкаталогах:' + tofile)
file.close()