class Product:

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.category}, {self.weight}'

class Shop:

    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        lst = (file.read())
        file.close()
        return lst

    def add(self, *products):
        file = open(self.__file_name, 'a')
        for i in range (len(products)):
            if products[i].name in self.get_products():
                print(f'{products[i].name} уже есть в магазине')
            else:
                file.write(f'{products[i]}\n')
        file.close()


s1 = Shop()
p1 = Product('Картофель', 50.5, 'Овощи')
p2 = Product('Макароны', 3.4, 'Бакалея')
p3 = Product('Яблоки', 55.2, 'Фрукты')
p4 = Product('Водка', 75, 'Алкоголь')
p5 = Product('Йогурт', 64, 'Молочные продукты')

print(p3) # __str__

print()
print('• Первое добавление — Картофель, макароны, яблоки')
s1.add(p1, p2, p3)
print('••• Что теперь есть в магазине:')
print(s1.get_products())

print('• Второе добавление — Макароны, яблоки, водка')
s1.add(p2, p3, p4)
print('••• Что теперь есть в магазине:')
print(s1.get_products())

print('• Третье добавление — Яблоки, водка, йогурт')
s1.add(p3, p4, p5)
print('••• Что теперь есть в магазине:')
print(s1.get_products())