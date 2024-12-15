class Iterator:
    pointer = 0

    def __init__(self, start, stop, step = 1):
        self.start = start
        self.stop = stop
        self.step = step
        if (self.start < self.stop and self.step <0) or (self.start > self.stop and self.step > 0):
            raise StepValueError('Неверный знак шага.')
        elif self.step == 0:
            raise StepValueError('Шаг не может быть нулевым.')

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        if (self.step > 0 and self.pointer > self.stop) or (self.step < 0 and self.pointer < self.stop):
            raise StopIteration
        else:
            self.pointer += self.step
            return self.pointer - self.step

class StepValueError(Exception):
    def __init__(self, message):
        self.message = message

##############################################################
print('\n•••••••')
try:
    iter1 = Iterator(100, 200, 0) # Нулевой шаг
    for i in iter1:
        print(i, end=' ')
except StepValueError as stepx:
    print(stepx.message)

print('\n•••••••')
try:
    iter2 = Iterator(-5, 1)
    for i in iter2:
        print(i, end=' ')
except StepValueError as stepx:
    print(stepx.message)

print('\n•••••••')
try:
    iter3 = Iterator(6, 15, 2)
    for i in iter3:
        print(i, end=' ')
except StepValueError as stepx:
    print(stepx.message)

print('\n•••••••')
try:
    iter4 = Iterator(5, 1, -1) # Интересно, почему PyCharm не пишет [step:] при отрицательном шаге?
    for i in iter4:
        print(i, end=' ')
except StepValueError as stepx:
    print(stepx.message)

print('\n•••••••')
try:
    iter5 = Iterator(10, 1) # Шаг по умолчанию <1> не приводит к конечному значению, а уводит от него...
    for i in iter5:
        print(i, end=' ')
except StepValueError as stepx:
    print(stepx.message) # ... поэтому пишем «Неверный знак шага».