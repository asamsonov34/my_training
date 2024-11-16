class Vehicle:

    # Атрибут класса, непереопределяемый в дочених классах: список разрешённых цветов
    __COLOR_VARIANTS = ['белый', 'чёрный', 'красный', 'серый', 'синий', 'голубой']

    def __init__(self, owner, model, hp, color):
        self.owner = owner
        self.__model = model
        self.__hp = hp
        self.__color = color

    def get_model(self):
        print(f'Модель: {self.__model}')

    def get_hp(self):
        print(f'Мощность двигателя: {self.__hp} л. с.')

    def get_color(self):
        print(f'Цвет: {self.__color}')

    def print_info(self):
        self.get_model()
        self.get_hp()
        self.get_color()
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color.lower() # Чтобы в нашем «ПТС» было единообразие регистров
        else:
            print(f'Нельзя сменить цвет на {new_color}')

class Sedan(Vehicle):

    __PASSANGER_LIMIT = 5

car1 = Sedan('Толян', 'Жига', 60, 'белый')
car1.print_info()
print('••• Пробуем изменить цвет на «неуставной» •••')
car1.set_color('розовый')
print('••• Изменяем цвет на «уставной» и меняем владельца •••')
car1.set_color('ЧЁРНЫЙ') # (поменяет, но запишет в «ПТС» в нижнем регистре — см. определение функции <set_color>)
car1.owner = 'Серёга'
car1.print_info()