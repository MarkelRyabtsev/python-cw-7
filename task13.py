import math
from helper import Helper


class Task13:

    __task_number = 13

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print('Произведение элементов двух массивов, стоящих на нечетных позициях')
        print('----------------------------------------------------------')
        random_array_1 = helper.set_random_array(10, range(-10, 10), True)
        random_array_2 = helper.set_random_array(10, range(-10, 10), True)
        print(f'Массив 1: {random_array_1}')
        print(f'Массив 2: {random_array_2}')
        print('----------------------------------------------------------')
        odd_elements = self.__get_odd_elements(random_array_1) + self.__get_odd_elements(random_array_2)
        print(f'Нечетные элементы массивов: {odd_elements}')
        print(f'Их произведение: {math.prod(odd_elements)}')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __get_odd_elements(array: []) -> []:
        try:
            return array[::2]
        except Exception as e:
            print(f'Ошибка: {e}')
