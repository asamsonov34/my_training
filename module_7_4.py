from random import randint
# (О Великий Рандом, сделай нашу жизнь интереснее! Пусть даже и с помощью только целых чисел...)

team1_name = 'Незанюханные кодеры'
team2_name = 'Займёмся питонизмом!'
team1_num = randint(5, 10)
team2_num = randint(5, 10)
team1_score = randint(45, 50)
team2_score = randint(45, 50)
team1_time = team1_score * randint(179, 180)
team2_time = team2_score * randint(179, 180)
tasks_total = team1_score + team2_score
# Время не складываем, а берём большее из двух: от начала баттла до момента,
# когда была решена последняя задача — неважно, кем.
time_avg = round(max(team1_time, team2_time) / tasks_total, 1)

def challenge_result():
    if team1_score > team2_score or (team1_score == team2_score and team1_time < team2_time):
        result = f'победа команды «{team1_name}»!'
    elif team1_score < team2_score or (team1_score == team2_score and team1_time > team2_time):
        result = f'победа команды «{team2_name}»!'
    else:
        result = 'ничья!' # Вероятность, при рандомизированных счёте и времени, разумеется, невелика, но бывает.
    return result


print()
print('ИСПОЛЬЗОВАНИЕ «%»')
print('     Сегодня в команде «%(name)s» %(num)s участников,' % {'name': team1_name, 'num': team1_num})
print('     а в команде «%(name)s» %(num)s участников,' % {'name': team2_name, 'num': team2_num})
print()
print('ИСПОЛЬЗОВАНИЕ «format()»')
print('     Команда «{name}» решила {score} задач за {time} секунд,'
      .format(name = team1_name, score = team1_score, time = team1_time))
print('     а команда «{name}» решила {score} задач за {time} секунд.'
      .format(name = team2_name, score = team2_score, time = team2_time))
print()
print('ИСПОЛЬЗОВАНИЕ f-СТРОК')
print(f'     Итак, на нашем кодинг-баттле обеими командами (всего {team1_num + team2_num} человек){chr(10)}'
      f'     было решено {tasks_total} задач за {max(team1_time, team2_time)} секунд — в среднем, {time_avg}'
      f' секунд на задачу.')
print(f'     Объявляем результат нашего баттла: {challenge_result().upper()}') # Заглавными — для торжественности