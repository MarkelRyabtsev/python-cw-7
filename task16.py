from helper import Helper


class Task16:

    __task_number = 16

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Подсчет количества чисел в массиве, которые меньше заданного числа')
        print('----------------------------------------------------------')
        random_array = helper.set_random_array(10, range(1, 100), is_uniq=True)
        print(random_array)
        n = helper.set_natural_number('Задайте число: ')
        print('----------------------------------------------------------')
        print(f'Количество чисел, которые меньше {n}: {self.__get_count(random_array, n)}')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __get_count(array: [], n: int) -> int:
        try:
            return sum(element < n for element in array)
        except Exception as e:
            print(f'Ошибка: {e}')
