import math
import random


class Task5:

    __task_number = 5

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Даны действительные числа a, b, c, d, e - стороны пятиугольника. Найти площадь пятиугольника. '
              '\n(Определить процедуру вычисления площади треугольника по его сторонам.) ')
        print('----------------------------------------------------------')
        random_side = random.randint(1, 10)
        print(f'Сторона пятиугольника: {random_side}')
        print('----------------------------------------------------------')
        print(f'Площадь пятиугольника: {self.__get_area(random_side)}')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    def __get_area(self, side: int) -> float:
        try:
            height = self.__get_height(side)
            triangle_area = ((side / 2) * height) / 2
            return round(triangle_area * 5, 2)
        except Exception as e:
            print(f'Ошибка: {e}')

    @staticmethod
    def __get_height(side: int) -> float:
        try:
            return side / math.tan(36 * math.pi / 180)  # 360° / 10(кол-во треугольников в пятиугольнике) = 36°
        except Exception as e:
            print(f'Ошибка: {e}')
