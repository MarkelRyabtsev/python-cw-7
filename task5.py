class Task5:

    __task_number = 5

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Дан текстовый файл f, компоненты которого являются целыми числами. Получить файл g, образованный из'
              '\nфайла f исключением повторных вхождений одного и того же числа')
        print('----------------------------------------------------------')
        numbers = self.__get_numbers()
        self.__remove_duplicate_and_safe(numbers)
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

    def __remove_duplicate_and_safe(self, numbers: []):
        try:
            filtered_numbers = list(dict.fromkeys(numbers))
            self.__save_file(filtered_numbers)
        except Exception as e:
            print(f'Ошибка: {e}')

    def __save_file(self, numbers: []):
        try:
            with open(f'files/outputs/task_{self.task_number}_output.txt', "w") as output:
                if len(numbers) == 0:
                    output.write('Отсутствуют.')
                else:
                    for number in numbers:
                        output.write("".join(
                            f'{number}') + "\n")
            print(f'Файл сохранен как files/outputs/task_{self.task_number}_output.txt')
        except Exception as e:
            print(f'Ошибка: {e}')
