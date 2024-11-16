class Animal:
    alive = True # По умлочанию животное живое...
    fed = False  # ... и голодное

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}') # Если съедобно, насытится...
            self.fed = True
        else:
            print(f'{self.name} попытался съесть {food.name}') # ... а несъедобно — помрёт
            self.alive = False

class Plant:
    edible = False

    def __init__(self, name):
        self.name = name

# У классов, дочерних для классов Animal и Plant, собственных атрибутов и методов нет, поэтому обойдутся
# без собственных конструкторов (__init__). У Fruit только съедобность переопределим.

class Predator(Animal):
    pass

class Herbivore(Animal):
    pass

class Fruit(Plant):
    edible = True

class Flower(Plant):
    pass

print('••• Проверяем, всё ли правильно наследуется: •••')
a1 = Predator('Тамбовский волк')
a2 = Herbivore('Бычара питерский')
print(f'Тип: {type(a1).__name__}, название: {a1.name}, живой: {a1.alive}, сытый: {a1.fed}')
print(f'Тип: {type(a2).__name__}, название: {a2.name}, живой: {a2.alive}, сытый: {a2.fed}')
p1 = Flower('Клейстокактус Штрауса')
p2 = Fruit('Спэлый пэрсик')
print(f'Тип: {type(p1).__name__}, название: {p1.name}, съедобный: {p1.edible}')
print(f'Тип: {type(p2).__name__}, название: {p2.name}, съедобный: {p2.edible}')
print('••• Проверяем работу метода eat(): •••')
print(f'{a1.name} живой: {a1.alive}')
print(f'{a2.name} сытый: {a2.fed}')
a1.eat(p1)
a2.eat(p2)
print(f'{a1.name} живой: {a1.alive}')
print(f'{a2.name} сытый: {a2.fed}')