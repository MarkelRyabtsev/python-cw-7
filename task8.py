import math
import random
from helper import Helper


class Task8:

    __task_number = 8

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Даны отрезки a,b,c и d. Для каждой тройки этих отрезков, из которых можно построить треугольник, '
              '\nнапечатать площадь данного треугольника. Определить процедуру Plo(x,y,z), выводящую площадь '
              '\nтреугольника со сторонами x,y и z, если такой треугольник существует')
        print('----------------------------------------------------------')
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        c = random.randint(1, 10)
        d = random.randint(1, 10)
        print(f'a = {a}, b = {b}, c = {c}, d = {d}')
        print('----------------------------------------------------------')
        print(f"Треугольник abc - {f'существует, площадь = {self.plo(a,b,c)}' if self.__is_exist(a,b,c) else 'не существует'} ")
        print(f"Треугольник abd - {f'существует, площадь = {self.plo(a,b,d)}' if self.__is_exist(a,b,d) else 'не существует'} ")
        print(f"Треугольник bcd - {f'существует, площадь = {self.plo(b,c,d)}' if self.__is_exist(b,c,d) else 'не существует'} ")
        print(f"Треугольник acd - {f'существует, площадь = {self.plo(a,c,d)}' if self.__is_exist(a,c,d) else 'не существует'} ")
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def plo(x: int, y: int, z: int) -> float:
        half_p = (x + y + z) / 2
        area = math.sqrt(half_p * (half_p - x) * (half_p - y) * (half_p - z))
        return round(area, 2)

    @staticmethod
    def __is_exist(x: int, y: int, z: int) -> bool:
        try:
            return x < y + z and y < x + z and z < x + y
        except Exception as e:
            print(f'Ошибка: {e}')
