import re


class Task15:

    __task_number = 15

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Дан текстовый файл f. Записать в файл g компоненты файла f в обратном порядке. Даны текстовые'
              '\nфайлы m и n. Записать в файл h сначала компоненты файла m, затем - компоненты'
              '\nфайла n с сохранением порядка')
        print('----------------------------------------------------------')
        text_a = self.__get_text('a')
        text_b_1 = self.__get_text('b_1')
        text_b_2 = self.__get_text('b_2')
        self.__do_task_a(text_a)
        print('----------------------------------------------------------')
        self.__do_task_b(text_b_1, text_b_2)
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    def __get_text(self, variant: str) -> str:
        try:
            with open(f'files/inputs/task_{self.task_number}_input_{variant}.txt') as f:
                return f.read()
        except Exception as e:
            print(f'Ошибка: {e}')

    def __do_task_a(self, text: str):
        try:
            text_components = re.findall(r"[\w']+", text)
            self.__save_file(' '.join(text_components[::-1]), 'a')
        except Exception as e:
            print(f'Ошибка: {e}')

    def __do_task_b(self, text_m: str, text_n: str):
        try:
            self.__save_file(text_m + " " + text_n, 'b')
        except Exception as e:
            print(f'Ошибка: {e}')

    def __save_file(self, text: [], task_variant: str):
        try:
            with open(f'files/outputs/task_{self.task_number}_output_{task_variant}.txt', "w") as output:
                output.write(text)
            print(f'{task_variant}) Файл сохранен как files/outputs/task_{self.task_number}_output_{task_variant}.txt')
        except Exception as e:
            print(f'Ошибка: {e}')
