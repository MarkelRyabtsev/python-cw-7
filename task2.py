import math


class Task2:

    __task_number = 2

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Дан текстовый файл f, компоненты которого являются целыми числами. Получить в файле g все '
              '\nкомпоненты файла f:'
              '\n   а) являющимися четными числами;'
              '\n   б) делящиеся на 3 и не делящиеся на 7;'
              '\n   в) являющимися точными квадратами.')
        print('----------------------------------------------------------')
        numbers = self.__get_numbers()
        print('----------------------------------------------------------')
        self.__do_task_a(numbers)
        print('----------------------------------------------------------')
        self.__do_task_b(numbers)
        print('----------------------------------------------------------')
        self.__do_task_c(numbers)
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    def __get_numbers(self) -> []:
        try:
            numbers_array = []
            with open(f'files/inputs/task_{self.task_number}_input.txt') as f:
                for line in f:
                    splitted_line = line.split(' ')
                    for number in splitted_line:
                        if number.isnumeric():
                            numbers_array.append(int(number))
            return numbers_array
        except Exception as e:
            print(f'Ошибка: {e}')

    def __do_task_a(self, numbers: []):
        try:
            filtered_numbers = []
            for number in numbers:
                if number % 2 == 0:
                    filtered_numbers.append(number)
            self.__save_file(filtered_numbers, 'a')
        except Exception as e:
            print(f'Ошибка: {e}')

    def __do_task_b(self, numbers: []):
        try:
            filtered_numbers = []
            for number in numbers:
                if number % 3 == 0 and number % 7 != 0:
                    filtered_numbers.append(number)
            self.__save_file(filtered_numbers, 'b')
        except Exception as e:
            print(f'Ошибка: {e}')

    def __do_task_c(self, numbers: []):
        try:
            filtered_numbers = []
            for number in numbers:
                if math.sqrt(number).is_integer():
                    filtered_numbers.append(number)
            self.__save_file(filtered_numbers, 'c')
        except Exception as e:
            print(f'Ошибка: {e}')

    def __save_file(self, numbers: [], task_variant: str):
        try:
            with open(f'files/outputs/task_{self.task_number}_output_{task_variant}.txt', "w") as output:
                if len(numbers) == 0:
                    output.write('Отсутствуют.')
                else:
                    for number in numbers:
                        output.write("".join(
                            f'{number}') + "\n")
            print(f'{task_variant}) Файл сохранен как files/outputs/task_{self.task_number}_output_{task_variant}.txt')
        except Exception as e:
            print(f'Ошибка: {e}')
