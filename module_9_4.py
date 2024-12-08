import random
from random import choices

# Lambda-функция:

first = 'Мама мыла раму'
second = 'Рамена мало было'

print(f'••• Вывод для секции «Lambda-функция»:\n{list(map(lambda x, y: x == y, first, second))}')

# Замыкание:

def get_advanced_writer(file_name):

    def write_everything(*data_set):
        filedata = '\n'.join(map(str, data_set))
        file = open(file_name, 'w', encoding='utf-8')
        file.write(filedata)
        file.close()

    return write_everything

write = get_advanced_writer('module_9_4_output.txt')
write('Это строковые данные', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'], 'А строкой ниже будет словарь:',
      {'мама': 'дома', 'папа': 'на работе', 'дети': 'в школе'})

# Метод __call__

class MysticBall:

    def __init__(self, *args):
        self.args = args

    def __call__(self, *args):
        return random.choice(self.args)

my_ball = MysticBall('Воистину так!', 'Не бывать тому!', 'Темна вода во облацех...')

r = 15 # СКОЛЬКО РАЗ "ОБРАТИТЬСЯ К МАГИЧЕСКОМУ ШАРУ"

print('••• Вывод для секции «Метод __call__»')
for i in range(r):
    print(my_ball())