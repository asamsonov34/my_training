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

    def __len__(self):
        return self.num_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.num_of_floors}'

h1 = House('Мегахижина Дяди Тома', 9) # дань памяти Г. Бичер-Стоу
h2 = House('ИзНаКурНож', 5) # дань памяти А. и б. Стругацких

# h1.go_to(6)
# h2.go_to(0)

print(h1)
print(len(h1))
print(h2)
print(len(h2))