from helper import Helper


class Task10:
    __task_number = 10

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Вывести все четырехзначные числа, в которых цифры не повторяются')
        print('----------------------------------------------------------')
        self.__print_numbers(helper)
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __print_numbers(helper: Helper):
        try:
            unique_numbers = list()
            for number in range(1000, 9999):
                unique = []
                for char in str(number):
                    if char not in unique:
                        unique.append(char)
                    else:
                        break
                if number == int(''.join(unique)):
                    unique_numbers.append(number)
            helper.print_long_array(unique_numbers)
        except Exception as e:
            print(f'Ошибка: {e}')
