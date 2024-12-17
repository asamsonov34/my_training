# ДЗ "Потоки на классах"

import threading
import time
from time import sleep


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.enemy_cnt = 100 # Раз у всех потоков, рождённых от Knight, по 100 врагов, чего б не засунуть в конструктор.
        self.delay = 1 # Опять-таки, у всех потоков задержка 1 сек — ну, типа, «игровой день».

    # Эта функция нужна только для согласования форм слов с числами. Можно было бы обойтись, но я не смог:
    # меня моё первое образование загрызло бы (лингвистика).
    def word_forms(self, cnt):
        if cnt in range(5, 20) or str(cnt)[-1] in ['5', '6', '7', '8', '9', '0']:
            forms = ('дней', 'мужеложцев', 'осталось')
        elif str(cnt)[-1] == '1':
            forms = ('день', 'мужеложец', 'остался')
        else:
            forms = ('дня', 'мужеложца', 'осталось')
        return forms

    def run(self):
        days = 0
        print(f'Сэр {self.name} вышел на битву с мужеложцами! ')
        while self.enemy_cnt:
            time.sleep(self.delay)
            days += 1
            self.enemy_cnt -= self.power
            if self.enemy_cnt < 0:
                self.enemy_cnt = 0
            print(f'Сэр {self.name} бьётся {days} {self.word_forms(days)[0]}. В живых {self.word_forms(self.enemy_cnt)[2]}'
                  f' {self.enemy_cnt} {self.word_forms(self.enemy_cnt)[1]}. ')
        print(f'••• ПОБЕДА! Сэр {self.name} покрошил всех мужеложцев спустя {days} {self.word_forms(days)[0]}! ')

knight1 = Knight('Квадратный Пупок', 3)
knight2 = Knight('Полторы Ягодицы', 5)
knight1.start()
sleep(0.001) # Придержим запуск 2-го потока на 1 мс (см. комментарий в конце).
knight2.start()

# Если не придержать второй поток, то иногда вывод от двух потоков настолько одновременный, что оба вывода
# залазят в одну строку, и далее пустая строка. Это чисто из эстетических соображений — некрасиво выглядит.
# Можете закомментить строку <41. sleep(0.001)> и посмотреть (бывает не при каждом запуске). А если это из-за
# того, что я что-то сделал не так, буду рад, если намекнёте в комментариях преподавателя, в чём беда.