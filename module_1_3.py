name = "Мегамикрокот"
print("Имя:", name)
age = 9
print("Возраст:", age) # integer type
incr = '1' # string type, cannot be added to an integer, but...
age = age + int(incr) # to make compatible for adding to the age
print("Изменённый возраст:", age)
is_student = True
is_human = False
if is_student: ru_rpl = "А то!" # just to see if "==True" in a condition can be ommitted, like in VBA
else: ru_rpl = "Не-а!"
print("Является ли студентом:", ru_rpl)
if not is_human: ru_rpl = "Отнюдь." # just to see if verbal negation is possible, like in VBA
else: ru_rpl = "Безусловно"
print("Является ли человеком:", ru_rpl)
# Let us try manual input
incr = input("На сколько ещё изменить возраст? Введите целое или дробное число: ")
while True:
        try:
            age = float(age) + float(incr)
            if float(age) - float(int(age)) == 0:
                age = int(age)
            else:
                age = float(age)
            break
        except ValueError:
            incr = input("Нет, введите ЦЕЛОЕ ЧИСЛО или ДРОБЬ С ДЕСЯТИЧНОЙ ТОЧКОЙ: ")

print("Вручную изменённый возраст: ", age)
