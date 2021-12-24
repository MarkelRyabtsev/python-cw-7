import random


class Student:

    def __init__(self, student_id, first_name, last_name, class_number, class_letter):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.class_number = class_number
        self.class_letter = class_letter


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Helper:

    @staticmethod
    def set_some_natural_numbers(description: str, count: int) -> tuple:
        while True:
            try:
                value = tuple(int(x.strip()) for x in input(f'{description} : ').split(' '))
                if len(value) == count:
                    return value
                else:
                    print(f'Введите {count} числа!')
            except:
                print('Введенные значения не являются натуральными числами, повторите!')
                continue

    @staticmethod
    def set_natural_number(description: str, numbers_range: range = None, all_numbers: bool = False) -> int:
        while True:
            try:
                value = int(input(f'{description} : '))
                if not all_numbers:
                    if value < 1:
                        print('Число должно быть больше 0!')
                        continue
                if numbers_range is not None and value not in numbers_range:
                    print(f'Введенное число должно быть в диапозоне от {numbers_range.start} до {numbers_range.stop}!')
                    continue
                return value
            except:
                print('Введенное значение не является натуральным числом, повторите!')
                continue

    @staticmethod
    def set_random_array(n: int, values_range: range, is_uniq: bool = False) -> []:
        random_array = []
        for i in range(0, n):
            random_value = random.randint(values_range.start, values_range.stop)
            if is_uniq:
                while True:
                    if random_value not in random_array:
                        break
                    else:
                        random_value = random.randint(values_range.start, values_range.stop)
            random_array.insert(i, random_value)
        return random_array

    @staticmethod
    def set_random_symbol_matrix(m: int) -> [[]]:
        random_array = []
        for i in range(0, m):
            row = []
            for a in range(0, m):
                row.insert(a, chr(random.randint(48, 65)))
            random_array.insert(i, row)
        return random_array

    @staticmethod
    def print_list_symbol_matrix(list_matrix: [[[]]]):
        current_matrix = 0
        current_row = 0
        while True:
            if current_matrix == len(list_matrix):
                current_row += 1
                current_matrix = 0
                print()
            for i in (list_matrix[current_matrix])[current_row]:
                print(f'[{i}]', end='')
            print('  ', end='')
            current_matrix += 1
            if current_row == len((list_matrix[0])[0]) - 1 and current_matrix == len(list_matrix):
                print()
                break

    @staticmethod
    def print_long_array(array: []):
        count = 1
        print('[', end='')
        for element in array:
            if count == len(array):
                print(f'{element}', end='')
            elif count % 15 != 0:
                print(f'{element}, ', end='')
            else:
                print(f'{element},')
            count += 1
        print(']')

    @staticmethod
    def get_random_point() -> Point:
        return Point(x=random.randint(-10, 10), y=random.randint(-10, 10))
