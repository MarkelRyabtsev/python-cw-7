import copy
from helper import Helper


class Task6:

    __task_number = 6

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Даны три символьные матрицы. '
              '\n a) ту матрицу, где есть хотя бы одна гласная - транспонировать; '
              '\n b) в той матрице, на главной диагонали которой все цифры, найти наименьшую и удалить '
              '\nсоответствующую строку')
        print('----------------------------------------------------------')
        print('Исходные матрицы')
        random_matrix_1 = helper.set_random_symbol_matrix(5)
        random_matrix_2 = helper.set_random_symbol_matrix(5)
        random_matrix_3 = helper.set_random_symbol_matrix(5)
        helper.print_list_symbol_matrix([random_matrix_1, random_matrix_2, random_matrix_3])
        print('----------------------------------------------------------')
        print('Вариант A')
        task_a_matrix_1, task_a_matrix_2, task_a_matrix_3 = self.__check_a(random_matrix_1, random_matrix_2,
                                                                           random_matrix_3)
        helper.print_list_symbol_matrix([task_a_matrix_1, task_a_matrix_2, task_a_matrix_3])
        print('----------------------------------------------------------')
        print('Вариант B')
        task_b_matrix_1, task_b_matrix_2, task_b_matrix_3 = self.__check_b(random_matrix_1, random_matrix_2,
                                                                           random_matrix_3)
        helper.print_list_symbol_matrix([task_b_matrix_1, task_b_matrix_2, task_b_matrix_3])
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    def __check_a(self, matrix_1: [[]], matrix_2: [[]], matrix_3: [[]]) -> tuple[[[]], [[]], [[]]]:
        try:
            new_matrix_1 = copy.deepcopy(matrix_1)
            new_matrix_2 = copy.deepcopy(matrix_2)
            new_matrix_3 = copy.deepcopy(matrix_3)
            if self.__is_has_vowel(matrix_1):
                new_matrix_1 = self.__transpose_matrix(matrix_1)
            if self.__is_has_vowel(matrix_2):
                new_matrix_2 = self.__transpose_matrix(matrix_2)
            if self.__is_has_vowel(matrix_3):
                new_matrix_3 = self.__transpose_matrix(matrix_3)
            return new_matrix_1, new_matrix_2, new_matrix_3
        except Exception as e:
            print(f'Ошибка: {e}')

    def __check_b(self, matrix_1: [[]], matrix_2: [[]], matrix_3: [[]]) -> tuple[[[]], [[]], [[]]]:
        try:
            new_matrix_1 = copy.deepcopy(matrix_1)
            new_matrix_2 = copy.deepcopy(matrix_2)
            new_matrix_3 = copy.deepcopy(matrix_3)
            if self.__is_diagonal_with_numbers(matrix_1):
                new_matrix_1 = self.__remove_min_number(matrix_1)
            if self.__is_diagonal_with_numbers(matrix_2):
                new_matrix_2 = self.__remove_min_number(matrix_2)
            if self.__is_diagonal_with_numbers(matrix_3):
                new_matrix_3 = self.__remove_min_number(matrix_3)
            return new_matrix_1, new_matrix_2, new_matrix_3
        except Exception as e:
            print(f'Ошибка: {e}')

    def __is_has_vowel(self, matrix: [[]]) -> bool:
        try:
            for row in matrix:
                for i in range(0, len(row)):
                    if self.__is_vowel(str(row[i])):
                        return True
            return False
        except Exception as e:
            print(f'Ошибка: {e}')

    @staticmethod
    def __remove_min_number(matrix: [[]]) -> [[]]:
        try:
            changed_matrix = copy.deepcopy(matrix)
            diagonal = [int(changed_matrix[i][i]) for i in range(len(changed_matrix))]
            min_value = int(min(diagonal))
            for i in range(len(changed_matrix)):
                if int(changed_matrix[i][i]) == min_value:
                    changed_matrix[i][i] = ' '
            return changed_matrix
        except Exception as e:
            print(f'Ошибка: {e}')

    @staticmethod
    def __transpose_matrix(matrix: [[]]) -> [[]]:
        zipped_rows = zip(*matrix)
        return [list(row) for row in zipped_rows]

    @staticmethod
    def __is_vowel(letter: str) -> bool:
        try:
            return letter.lower() in ['a', 'e', 'i', 'o', 'u']
        except Exception as e:
            print(f'Ошибка: {e}')

    @staticmethod
    def __is_diagonal_with_numbers(matrix: [[]]) -> bool:
        try:
            diagonal = [matrix[i][i] for i in range(len(matrix))]
            if all(str(element).isnumeric() for element in diagonal):
                return True
            return False
        except Exception as e:
            print(f'Ошибка: {e}')
