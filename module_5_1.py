class House:

    def __init__(self, name, num_of_floors):
        self.name = name
        self.num_of_floors = num_of_floors

    def go_to(self, new_floor):
        if new_floor > self.num_of_floors or new_floor < 1: # Принимаем, что нет цокольного (0) и подземных (<1) этажей
            print(f'В доме «{self.name}» нет такого этажа')
        else:
            for i in range(new_floor):
                print(i+1)
            print(f'Вы прибыли на {int(new_floor)} этаж дома «{self.name}»')

h1 = House('Развалюха-на-холме', 16)
h2 = House('Небоскрёб-недоносок', 3)

h1.go_to(6)
h2.go_to(0)