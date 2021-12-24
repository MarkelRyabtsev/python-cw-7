import math
import random


class Task9:

    __task_number = 9

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Даны длины a,b и c сторон некоторого треугольника. Найти медианы треугольника, сторонами которого '
              '\nявляются медианы исходного треугольника. Длина медианы, проведенной к стороне a, равна'
              '\n1/2 * √(2b^2 + 2c^2 - a^2)')
        print('----------------------------------------------------------')
        a, b, c = self.__get_existing_triangle()
        print(f'Стороны треугольника: a = {a}, b = {b}, c = {c}')
        print('----------------------------------------------------------')
        median_a, median_b, median_c = self.__get_medians(a, b, c)
        print(f'Медианы треугольника: Ma = {median_a}, Mb = {median_b}, Mc = {median_c}')
        median_a_new, median_b_new, median_c_new = self.__get_medians(median_a, median_b, median_c)
        print(f'Медианы треугольника, сторонами которого являются медианы исходного '
              f'\nтреугольника : Ma\' = {median_a_new}, Mb\' = {median_b_new}, Mc\' = {median_c_new}')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __get_medians(a: float, b: float, c: float) -> tuple[float, float, float]:
        try:
            median_a = (math.sqrt(2 * (b ** 2) + 2 * (c ** 2) - a ** 2)) / 2
            median_b = (math.sqrt(2 * (a ** 2) + 2 * (c ** 2) - b ** 2)) / 2
            median_c = (math.sqrt(2 * (a ** 2) + 2 * (b ** 2) - c ** 2)) / 2
            return round(median_a, 2), round(median_b, 2), round(median_c, 2)
        except Exception as e:
            print(f'Ошибка: {e}')

    def __get_existing_triangle(self) -> tuple[int, int, int]:
        try:
            while True:
                x = random.randint(1, 10)
                y = random.randint(1, 10)
                z = random.randint(1, 10)
                if self.__is_exist(x, y, z):
                    return x, y, z
        except Exception as e:
            print(f'Ошибка: {e}')

    @staticmethod
    def __is_exist(x: int, y: int, z: int) -> bool:
        try:
            return x < y + z and y < x + z and z < x + y
        except Exception as e:
            print(f'Ошибка: {e}')
