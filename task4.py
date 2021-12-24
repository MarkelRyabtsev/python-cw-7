

class Task4:

    __task_number = 4

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Найти среднее арифметическое положительных элементов в массиве. Использовать процедуру для ввода '
              '\nэлементов массива и функцию для подсчета среднего арифметического')
        print('----------------------------------------------------------')
        array = []
        self.__enter_array_numbers(array)
        print('----------------------------------------------------------')
        print(f'Массив: {array}')
        print('----------------------------------------------------------')
        print(f'Среднее арифметическое положительных эл. = {self.__get_average_of_positive(array)}')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __enter_array_numbers(array: []):
        print(f'Вводите числа, для остановки введите "0" : ', end='')
        while True:
            try:
                value = float(input(
                    f'{array} : ' if len(array) > 0
                    else ""
                ))
                if value == 0:
                    if len(array) == 0:
                        print(f'Массив не содержит значений! Введите значение : ', end='')
                        continue
                    else:
                        break
                array.append(value)
            except:
                print('Введенное значение не является числом, повторите!')
                continue

    @staticmethod
    def __get_average_of_positive(array: []) -> float:
        try:
            positive_elements = [element for element in array if element >= 0]
            return sum(positive_elements) / len(positive_elements)
        except Exception as e:
            print(f'Ошибка: {e}')
