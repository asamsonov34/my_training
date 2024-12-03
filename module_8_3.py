class Car:

    def __init__(self, model, vin_num, reg_num):
        self.model = model
# Проверялки только так получилось вызвать. Хотите показать способ получше —
# черкните в Телегу @ASamsonov34T003, спасибо.
        if self._Car__isvalid_vin(vin_num):
            self.__vin_num = vin_num
        if self._Car__isvalid_reg(reg_num):
            self.__reg_num = reg_num

    def __isvalid_vin(cls, vin_num):
       if not isinstance(vin_num, int):
           raise BadVinNum('Неверный тип VIN-номера.')
       elif vin_num not in range(1000000, 10000000):
           raise BadVinNum('Неверный диапазон для VIN-номера.')
       else:
           return True

    def __isvalid_reg(cls, reg_num):
        if not isinstance(reg_num, str):
            raise BadRegNum('Некорректный тип данных для госномераю')
        elif len(reg_num) != 6:
            raise BadRegNum('Неверная длина госномера.')
        else:
            return True


class BadVinNum(Exception):
    def __init__(self, message):
        self.message = message

class BadRegNum(Exception):
    def __init__(self, message):
        self.message = message

# Начинаем создавать экземпляры класса <Car>
print('—————————————————————————————————————————————————————————————————————————')
try:
    first = Car('Жыга', 1234567, 'ау123ы')
except BadVinNum as vx:
    print(vx.message)
except BadRegNum as rx:
    print(rx.message)
else:
    print(f'Смастырен драндулет модели «{first.model}» с VINом <{first._Car__vin_num}>'
          f'и госномером <{first._Car__reg_num}>')

print('—————————————————————————————————————————————————————————————————————————')
try:
    first = Car('БуБумер', 987654321, 'аа777а')
except BadVinNum as vx:
    print(vx.message)
except BadRegNum as rx:
    print(rx.message)
else:
    print(f'Смастырен драндулет модели «{first.model}» с VINом <{first._Car__vin_num}>'
          f'и госномером <{first._Car__reg_num}>')

print('—————————————————————————————————————————————————————————————————————————')
try:
    first = Car('МерсюкНах!', 7777777, 333333)
except BadVinNum as vx:
    print(vx.message)
except BadRegNum as rx:
    print(rx.message)
else:
    print(f'Смастырен драндулет модели «{first.model}» с VINом <{first._Car__vin_num}>'
          f'и госномером <{first._Car__reg_num}>')