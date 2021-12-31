class Task11:

    __task_number = 11

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Дан символьный файл f:'
              '\n   а) подсчитать число вхождений в файл сочетаний \'ab\';'
              '\n   б) определить входит ли в файл сочетание \'abcdefgh\';'
              '\n   в) подсчитать число вхождений в файл каждой из букв \'a\',\'b\',\'c\',\'d\',\'e\',\'f\' и'
              '\nвывести результат в виде таблицы:'
              '\na --> Na b --> Nb c --> Nc d --> Nd e --> Ne f --> Nf,'
              '\nгде Na, Nb, Nc, Nd, Ne, Nf - числа вхождений соответствующих букв.')
        print('----------------------------------------------------------')
        text = self.__get_text()
        self.__do_task_a(text)
        print('----------------------------------------------------------')
        self.__do_task_b(text)
        print('----------------------------------------------------------')
        self.__do_task_c(text)
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    def __get_text(self) -> str:
        try:
            with open(f'files/inputs/task_{self.task_number}_input.txt') as f:
                return f.read()
        except Exception as e:
            print(f'Ошибка: {e}')

    @staticmethod
    def __do_task_a(text: str):
        try:
            ab_count = text.lower().count('ab')
            print(f'а) Число вхождений сочетания \'ab\' в тексте: {ab_count}')
        except Exception as e:
            print(f'Ошибка: {e}')

    @staticmethod
    def __do_task_b(text: str):
        try:
            try:
                count = text.lower().count('abcdefgh')
                print(f'б) Сочетание \'abcdefgh\'{"" if count > 0 else " не"} входит в файл')
            except Exception as e:
                print(f'Ошибка: {e}')
        except Exception as e:
            print(f'Ошибка: {e}')

    @staticmethod
    def __do_task_c(text: str):
        try:
            vowel_dict = dict()
            for vowel in text:
                if vowel.lower() in 'abcdef':
                    if vowel.lower() in vowel_dict.keys():
                        vowel_dict[vowel.lower()] = vowel_dict[vowel.lower()] + 1
                    else:
                        vowel_dict[vowel.lower()] = 1
            print('в) Число вхождений в файл каждой из букв \'a\',\'b\',\'c\',\'d\',\'e\',\'f\'')
            for (vowel, count) in vowel_dict.items():
                print(f'{vowel} --> {count}')
        except Exception as e:
            print(f'Ошибка: {e}')
