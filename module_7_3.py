class WordsFinder:

    file_names = ()
    all_words = {}
    found = {}

    def __init__(self, *params):
        self.file_names = params
        for cur_file in params:
            with open(cur_file, 'r', encoding = 'utf-8') as file:
                filetext = file.read().lower()  # .split()
                for badchar in [',', '.', '=', '!', '?', ';', ':', ' - ', ' — ', '(', ')']:
                    filetext = filetext.replace(badchar, '')
                filetext = filetext.split()
                self.all_words.update({cur_file: filetext})
        # print(self.all_words)

    def get_all_words(self):
        return self.all_words

    def find(self, word):
        for fname in self.all_words.keys():
            if word in self.all_words.get(fname):
                lst = self.all_words.get(fname)
                for i in range(len(lst)):
                    if lst[i].lower() == word.lower():
                        self.found.update({fname: i+1})
                        break
                # self.found.update({fname: 1})
        return self.found

    def count(self, word):
        result = {}
        for fname in self.all_words.keys():
            if word in self.all_words.get(fname):
                lst = self.all_words.get(fname)
                cnt = 0
                for i in range(len(lst)):
                    if lst[i].lower() == word.lower():
                        cnt += 1
                result.update({fname: cnt})
        return result


finder = WordsFinder('module_7_3_1.txt', 'module_7_3_2.txt')
print(finder.get_all_words())
# print(f'Позиция первого вхождения в каждом файле: {finder.find('text')}')
# print(f'Кол-во вхождений в каждом файле: {finder.count('text')}')
# print(f'Позиция первого вхождения в каждом файле: {finder.find('успехов')}')
# print(f'Кол-во вхождений в каждом файле: {finder.count('успехов')}')