calls = 0

def count_calls():
    global calls
    calls += 1


def string_info(my_str):
    count_calls()
    return (len(my_str), my_str.upper(), my_str.lower())

def in_list (my_str, my_list):
    count_calls()
    is_memeber = False
    for i in range(len(my_list)):
        if my_list[i].lower() == my_str.lower():
            is_memeber = True
            break
        else:
            continue
    return is_memeber

print(string_info('ДоСтоПриМеЧаТельНость'))
print(string_info('ДлиНноШеЕе'))
print(string_info('КроКодилоОбраЗный'))
print(in_list('БлЯХа', ['бляха', 'муха', 'кукуха']))
print(in_list('пруха', ['бляха', 'муха', 'кукуха']))
print(calls)
