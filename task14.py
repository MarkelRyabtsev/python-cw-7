from helper import Helper


class Task14:

    __task_number = 14

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Определить максимальное число из четырех введенных, путем сравнения их сначала попарно, '
              '\nа затем результат между собой')
        print('----------------------------------------------------------')
        a, b, c, d = helper.set_some_natural_numbers('Введите 4 числа через пробел', 4)
        first_pair = a, b
        first_pair_result = self.__get_max_from_two(first_pair[0], first_pair[1])
        second_pair = c, d
        second_pair_result = self.__get_max_from_two(second_pair[0], second_pair[1])
        print(f'Первая пара: {first_pair[0]} {first_pair_result[1]} {first_pair[1]}')
        print(f'Вторая пара: {second_pair[0]} {second_pair_result[1]} {second_pair[1]}')
        final_pair = first_pair_result[0], second_pair_result[0]
        final_pair_result = self.__get_max_from_two(final_pair[0], final_pair[1])
        print(f'Итоговая пара: {final_pair[0]} {final_pair_result[1]} {final_pair[1]}')
        print('----------------------------------------------------------')
        print(f'Максимальное число: {final_pair_result[0]}')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __get_max_from_two(first: int, second: int) -> tuple[int, str]:
        try:
            if first > second:
                return first, '>'
            elif first < second:
                return second, '<'
            else:
                return first, '='
        except Exception as e:
            print(f'Ошибка: {e}')
