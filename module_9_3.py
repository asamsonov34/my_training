first = ['Strings', 'Student', 'Computers', 'Trash', 'Handler']
second = ['Строка', 'Урбан', 'Компьютер', 'Мусор', 'Обработчик']

res1 = (abs(len(x[0]) - len(x[1])) for x in zip(first, second) if len(x[0]) != len(x[1]))
res2 = (len(first[i]) == len(second[i]) for i in range(len(first)))

print(list(res1))
print(list(res2))
