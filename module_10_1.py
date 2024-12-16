import threading
import time
import datetime
from time import sleep

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding = 'utf-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово №{i + 1}\n')
            sleep(0.1)
        print(f'Завершилась запись в файл <{file_name}>')

# Поскольку при всех вызовах в главном потоке они всё равно вызываются последовательно, почему бы не сделать цикл
# вызовов, передавая заготовленные параметры из списка:

params = [[10, 'example1.txt'], [30, 'example2.txt'], [200, 'example3.txt'], [100, 'example4.txt']]
total_time = 0
for i in range(len(params)):
    t_beg = time.time()
    write_words(params[i][0], params[i][1])
    t_end = time.time()
    total_time += round((t_end - t_beg), 3)
    print(f'Время выполнения для <wordcount = {params[i][0]}>: {round((t_end - t_beg), 3)} сек. '
          f'({str(datetime.timedelta(seconds = t_end - t_beg))})')
print(f'Всего затрачено на выполнение всех вызовов: {total_time} сек. '
      f'({str(datetime.timedelta(seconds = t_end - t_beg))})')

t_beg = time.time()

thread1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thread4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread1.join()
thread2.join()
thread3.join()
thread4.join()

t_end = time.time()
print(f'Время выполнения для 4 вызовов, каждый в своём потоке: {round((t_end - t_beg), 3)} сек. '
      f'({str(datetime.timedelta(seconds = t_end - t_beg))})')