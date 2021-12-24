import re
from helper import Helper


class Task15:

    __task_number = 15

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} ДОДЕЛАТЬ -------------------------')
        print('Вычислить функцию z(x)=x^2 и сумму членов ряда y=pi^2-4*(cosx - cos2x/2^2 + cos3x/3^2 - ...)'
              '\nна диапазоне [-pi;pi]. Очередной элемент включается в сумму, если его значение по модулю превышает'
              '\nнекоторое заранее заданное число P, определяемое с требуемой точностью вычислений. P=0.001')
        print('----------------------------------------------------------')
        random_text = helper.get_random_short_text_eng()
        print(random_text)
        print('----------------------------------------------------------')
        formatted_text = helper.remove_line_feed(random_text)
        self.__print_count_and_remove_double_letters(formatted_text)
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    def __print_count_and_remove_double_letters(self, text: str):
        try:
            words_array = re.findall(r"[\w']+", text)
            words_array_changed = []
            for word in words_array:
                changed_word = self.__check_letters(word)
                words_array_changed.append(changed_word)
            new_text = ' '.join(words_array_changed)
            print(new_text)
            print('----------------------------------------------------------')
            new_words_array = re.findall(r"[\w']+", new_text)
            print(f'Количество слов: {len(new_words_array)}')
        except Exception as e:
            print(f'Ошибка: {e}')

    @staticmethod
    def __check_letters(word: str) -> str:
        try:
            new_word = list(word)
            if new_word[0] == new_word[len(word) - 1]:
                return ''
            else:
                return ' '.join([''.join(new_word), ''.join(new_word)])
        except Exception as e:
            print(f'Ошибка: {e}')
