class House:

    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, name, num_of_floors):
        self.name = name
        self.num_of_floors = num_of_floors

    def __del__(self):
        print(f'«{self.name}» развалился, но мы-то знаем, что он был.')

    def __len__(self):
        return self.num_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.num_of_floors}'

    def __eq__(self, other):
        return self.num_of_floors == other.num_of_floors

    def __lt__(self, other):
        return self.num_of_floors < other.num_of_floors

    def __gt__(self, other):
        return self.num_of_floors > other.num_of_floors

    def  __le__(self, other):
        return self.num_of_floors <= other.num_of_floors

    def __ge__(self, other):
        return self.num_of_floors >= other.num_of_floors

    def __ne__(self, other):
        return self.num_of_floors != other.num_of_floors

    def go_to(self, new_floor):
        if new_floor > self.num_of_floors or new_floor < 1: # Принимаем, что нет цокольного (0) и подземных (<1) этажей
            print(f'В доме «{self.name}» нет такого этажа')
        else:
            for i in range(new_floor):
                print(i+1)
            print(f'Вы прибыли на {int(new_floor)} этаж дома «{self.name}»')

    def __add__(self, value):
        self.num_of_floors = self.num_of_floors + value
        return self

    def __radd__(self, value):
        self.num_of_floors = value + self.num_of_floors
        return self

    def __iadd__(self, value):
        self.num_of_floors += value
        return self

    def __sub__(self, value):
        self.num_of_floors = self.num_of_floors - value
        return self

    def __rsub__(self, value):
        self.num_of_floors = value - self.num_of_floors
        return self

    def __isub__(self, value):
        self.num_of_floors -= value
        return self

    def __mul__(self, value):
        self.num_of_floors = self.num_of_floors * value
        return self

    def __rmul__(self, value):
        self.num_of_floors = value * self.num_of_floors
        return self

    def __imul__(self, value):
        self.num_of_floors *= value
        return self

    def __div__(self, value): # Интересно, почему «__div__» другого цвета?
        self.num_of_floors = self.num_of_floors / value
        return self

    def __rdiv__(self, value):
        self.num_of_floors = value / self.num_of_floors
        return self

    def __idiv__(self, value):
        self.num_of_floors /= value
        return self

# Проверяем, всё ли работает как надо в методе __new__:

h1 = House('НЕДОскрёб', 10)
print(House.houses_history)
h2 = House('Урбо-Теремок', 20)
print(House.houses_history)
h3 = House('Кроличья нора', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3
print(House.houses_history)