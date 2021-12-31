class Task7:

    __task_number = 7

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Дан текстовый файл f, компоненты которого являются целыми числами. Никакая из компонент файла не'
              '\nравна нулю. Числа в файле идут в следующем порядке: десять положительных, десять отрицательных,'
              '\nдесять положительных, десять отрицательных и т.д. Переписать компоненты файла f в файл g так,'
              '\nчтобы в файле g числа шли в следующем порядке:'
              '\n   а) пять положительных, пять отрицательных, пять положительных, пять отрицательных и т.д.;'
              '\n   б) двадцать положительных, двадцать отрицательных, двадцать положительных, двадцать'
              '\nотрицательных и т.д. (предполагается, что число компонент в файле f делится на 40)')
        print('----------------------------------------------------------')
        numbers = self.__get_numbers()
        self.__do_task_a(numbers)
        print('----------------------------------------------------------')
        self.__do_task_b(numbers)
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    def __get_numbers(self) -> []:
        try:
            numbers_array = []
            with open(f'files/inputs/task_{self.task_number}_input.txt') as f:
                for line in f:
                    splitted_line = line.split(' ')
                    for number in splitted_line:
                        numbers_array.append(int(number))
            return numbers_array
        except Exception as e:
            print(f'Ошибка: {e}')

    def __do_task_a(self, numbers: []):
        try:
            filtered_numbers_positive = []
            filtered_numbers_negative = []
            for number in numbers:
                if number > 0:
                    filtered_numbers_positive.append(number)
                else:
                    filtered_numbers_negative.append(number)
            filtered_numbers_joined = []
            positive_sliced = zip(*[iter(filtered_numbers_positive)] * 5)
            negative_sliced = zip(*[iter(filtered_numbers_negative)] * 5)
            for pair in zip(positive_sliced, negative_sliced):
                list_of_pairs = [i for t in pair for i in t]
                for ar in list_of_pairs:
                    filtered_numbers_joined.append(ar)
            self.__save_file(filtered_numbers_joined, 'a')
        except Exception as e:
            print(f'Ошибка: {e}')

    def __do_task_b(self, numbers: []):
        try:
            filtered_numbers_positive = []
            filtered_numbers_negative = []
            for number in numbers:
                if number > 0:
                    filtered_numbers_positive.append(number)
                else:
                    filtered_numbers_negative.append(number)
            filtered_numbers_joined = []
            positive_sliced = zip(*[iter(filtered_numbers_positive)] * 20)
            negative_sliced = zip(*[iter(filtered_numbers_negative)] * 20)
            for pair in zip(positive_sliced, negative_sliced):
                list_of_pairs = [i for t in pair for i in t]
                for ar in list_of_pairs:
                    filtered_numbers_joined.append(ar)
            self.__save_file(filtered_numbers_joined, 'b')
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
