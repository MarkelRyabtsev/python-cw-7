class Task9:

    __task_number = 9

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Дан текстовый файл f, компоненты которого являются целыми числами. Записать в файл g наибольшее'
              '\nзначение первых пяти компонент файла f, затем - следующих пяти компонент и т.д. Если в последней'
              '\nгруппе окажется менее пяти компонент, то последняя компонента файла g должна быть равна наибольшей'
              '\nиз компонент файла f, образующих последнюю (неполную) группу')
        print('----------------------------------------------------------')
        numbers = self.__get_numbers()
        print('----------------------------------------------------------')
        self.__do_task(numbers)
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

    def __do_task(self, numbers: []):
        try:
            sliced_numbers = list(zip(*[iter(numbers)] * 5))
            numbers_from_max = []
            for five_numbers in sliced_numbers:
                numbers_from_max.append(max(five_numbers))
            if len(numbers) % 5 != 0:
                numbers_from_max.append(max(numbers[-(len(numbers) - (int(len(numbers) / 5)) * 5):]))
            self.__save_file(numbers_from_max)
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
