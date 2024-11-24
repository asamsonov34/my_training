def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding = 'utf-8')
    strings_positions = {}
    tpl = ()
    for i in range(len(strings)):
        tpl = (i + 1, file.tell())
        if i < len(strings) - 1:
            file.write(f'{strings[i]}\n')
        else:
            file.write(strings[i])
        strings_positions.update({tpl: strings[i]})
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('strings.txt', info)
for elem in result.items():
    print(elem)