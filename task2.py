import math
from helper import Helper, Point


class Task2:

    __task_number = 2

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Используя функцию нахождения длины отрезка (по теореме Пифагора), найти длину периметра и площадь '
              '\nтреугольника, заданного координатами своих вершин')
        print('----------------------------------------------------------')
        a_point = helper.get_random_point()
        b_point = helper.get_random_point()
        c_point = helper.get_random_point()
        print(f'A({a_point.x}, {a_point.y})')
        print(f'B({b_point.x}, {b_point.y})')
        print(f'C({c_point.x}, {c_point.y})')
        print('----------------------------------------------------------')
        ab_vector = self.__get_vector_length(a_point, b_point)
        bc_vector = self.__get_vector_length(b_point, c_point)
        ac_vector = self.__get_vector_length(a_point, c_point)
        print(f'Длина AB = {ab_vector}')
        print(f'Длина BC = {bc_vector}')
        print(f'Длина AC = {ac_vector}')
        print('----------------------------------------------------------')
        print(f'Периметр = {self.__get_perimeter(ab_vector, bc_vector, ac_vector)}')
        print(f'Площадь = {self.__get_area(ab_vector, bc_vector, ac_vector)}')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __get_vector_length(first: Point, second: Point) -> float:
        try:
            return round(math.sqrt((second.x - first.x) ** 2 + (second.y - first.y) ** 2), 2)
        except Exception as e:
            print(f'Ошибка: {e}')

    @staticmethod
    def __get_perimeter(vector_1: float, vector_2: float, vector_3: float) -> float:
        try:
            return round(vector_1 + vector_2 + vector_3, 2)
        except Exception as e:
            print(f'Ошибка: {e}')

    @staticmethod
    def __get_area(vector_1: float, vector_2: float, vector_3: float) -> float:
        try:
            half_perimeter = (vector_1 + vector_2 + vector_3) / 2
            return round(math.sqrt(half_perimeter * (half_perimeter - vector_1) * (half_perimeter - vector_2) * (half_perimeter - vector_3)), 2)
        except Exception as e:
            print(f'Ошибка: {e}')
