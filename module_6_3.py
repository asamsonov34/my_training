from random import randint

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self._coords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        if self._coords[2] + (dz * self.speed) >= 0:
            self._coords[0] += (dx * self.speed)
            self._coords[1] += (dy * self.speed)
            self._coords[2] += (dz * self.speed)
        else:
            print('Не, я вглубь не умею, я не нырец!')

    def get_coords(self):
        print(f'X: {self._coords[0]}, Y: {self._coords[1]}, Z: {self._coords[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print('Нападать не буду, я мирная животинка :)')
        else:
            print('Попячься, ща как нападу!')

    def speak(self):
        print(f'{type(self).__name__} звучит вот так: «{self.sound}»')

class Bird(Animal):
    beak = True
    sound = 'Чирик!'

    def lay_eggs(self):
        print(f'По вашему заданию отложены яйца в количестве {randint(1, 4)} шт.!')

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        # В примере к заданию — целое число, а деление даёт float, поэтому округляем. С точностью округления
        # не заморачиваемся, юзаем round(). Да, с math или decimal было бы точнее, но мы сейчас не про это.
        self._coords[2] -= round(abs(dz) / 2 * self.speed) # «С учётом скорости» — понял, как «умножить на скорость».

class PoisonousAnimal:
    _DEGREE_OF_DANGER = 8

class Duckbill(PoisonousAnimal, AquaticAnimal, Bird):
    sound = 'Уррр!' # https://yandex.ru/video/preview/7946484639187040936 и другие видео про звуки утконоса

db = Duckbill(10)
print(f'Утконос живой: {db.live}')
print(f'У утконоса есть клюв: {db.beak}')

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_coords()
db.dive_in(9) # В примере dz = 6, и Z в итоге равно нулю, но хотелось убедиться, что и в глубину может (Z выходит -15).
db.get_coords()

db.lay_eggs()