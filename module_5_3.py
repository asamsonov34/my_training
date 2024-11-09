class House:

    def __init__(self, name, num_of_floors):
        self.name = name
        self.num_of_floors = num_of_floors

    def __len__(self):
        return self.num_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.num_of_floors}'

    # Операторы сравнения, по заданию, должны сравнивать количество этажей и возвращать булев результат:

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

# А арифметические операторы, как я понимаю, должны возвращать класс во всей его целостности
# (ну, экземпляр класса), только с именёнными, в соответствии с арифметическими действиями,
# значениями числа этажей:

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

h1 = House('Дом Артура Дента', 10) # дань памяти Дугласа Адамса
h2 = House('Дом пионеров', 20) # дань памяти стране, где я родился

# Чтобы было легче проверить, всё ли я сделал правильно в соответствии с заданием,
# проверочные действия прямо скопировал из задания:

print(h1)
print(h2)
print(h1 == h2) # __eq__
h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)
h1 += 10 # __iadd__
print(h1)
h2 = 10 + h2 # __radd__
print(h2)
print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__

# Вывод получился такой же, как в задании — значит, всё правильно. Но если я, по Вашему мнению,
# что-то понял неправильно (а я специально в комментариях писал, что и как я понимаю), буду рад,
# если потыкаете меня носом куда надо в Телеге: https://t.me/ASamsonov34T003 (ну, или @ASamsonov34T003).
# Заранее благодарю!.