# Ну, не сердитесь, я опять попробовал что-то, что не входит в задание

name = "Мегамикрокот"
print("Имя:", name)
age = 9
print("Возраст:", age) # integer type
incr = '1' # string type, cannot be added to an integer, but...
age = age + int(incr) # to make compatible for adding to the age
print("Изменённый возраст:", age)
is_student = False
if is_student: ru_rpl = "А то!" # just to see if "==True" in a condition can be ommitted, like in VBA
else: ru_rpl = "Не-а!"
print("Является ли студентом:", ru_rpl)
if not is_student: ru_rpl = "Отнюдь." # just to see if verbal negation is possible, like in VBA
else: ru_rpl = "Безусловно"
print("Является ли студентом:", ru_rpl)
incr = input("На сколько ещё изменить возраст? Введите целое число: ")
while True:
        try:
            age = age + int(incr)
            break
        except ValueError:
            incr = input("Не-а, это не было целое число. Таки введите целое число: ")
print("Вручную изменённый возраст: ", age)