def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()

test_function()

try:
    inner_function()
except NameError:
    print('ОШИБКА: имя "inner_function" недоступно в глобальной области видимости')
