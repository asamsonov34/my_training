import time
from multiprocessing import Pool

def readinfo(fname):
    all_data = []
    with open(fname, 'r') as file:
        while True:
            str = file.readline()
            if str != '':
                all_data += str
            else:
                break

filenames = [f'./module_11_01-{number}.txt' for number in range(1, 5)]

# ПОМЕСТИЛ ПОСЛЕДОВАТЕЛЬНЫЙ И ПАРАЛЛЕЛЬНЫЙ ВЫЗОВЫ ВНУТРЬ ФУНКЦИЙ, ЧТОБЫ СДЕЛАТЬ ПОЛЬЗОВАТЕЛЬСКИЙ ВЫБОР ТИПА ЗАПУСКА.
# НЕ РАБОТАЕТ КАК НАДО — НАДО ПОНЯТЬ, ПОЧЕМУ. ЗАДАМ ВОПРОС В "ВОПРОСАХ К ПРЕПОДАВАТЕЛЮ". КОД С ПОЛЬЗОВАТЕЛЬСКИМ
# ВЫБОРОМ УБРАЛ ДО ТОГО, КАК ПОЙМУ, В ЧЁМ ДЕЛО, И КАК ИСПРАВИТЬ.

# А ПОКА — ВЫЗОВ В КОНЦЕ.

def sequential():
    t_beg = time.time()
    for f in filenames:
        readinfo(f)
    t_end = time.time()
    print(f'Время выполнения при последовательном вызове: {round((t_end - t_beg), 3)} сек.')

def parallel():
    if __name__ == '__main__':
        t_beg = time.time()
        with Pool() as pool:
            pool.map(readinfo, filenames)
        t_end = time.time()
        print(f'Время выполнения при параллельном вызове: {round((t_end - t_beg), 3)} сек.')

# sequential()
parallel()

# Вариант с пользовательским выбором отрабатывает нормально при выборе ПОСЛЕДОВАТЕЛЬНОГО выполнения,
# но не работает как надо, при выборе ПАРАЛЛЕЛЬНОГО выполнения. Ну, по крайней мере, так только две
# строки надо закомменчивать-раскомменчивать, а не по несколько строк...