import math
from helper import Helper, Point


class Task3:

    __task_number = 3

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Даны действительные числа х1, у1, х2, у2, …,х10, у10. Найти периметр десятиугольника, вершины '
              '\nкоторого имеют соответственно координаты (х1, у1), (х2, у2), …, (х10, у10). (Определить процедуру '
              '\nвычисления расстояния между двумя точками, заданными своими координатами.) ')
        print('----------------------------------------------------------')
        point_list = list()
        for i in range(0, 10):
            point_list.append(helper.get_random_point())
            print(f'Точка {i + 1} = ({point_list[i].x}, {point_list[i].y})')
        print('----------------------------------------------------------')
        vector_list = list()
        for i in range(0, 9):
            if i != 9:
                vector_list.append(self.__get_vector_length(point_list[i], point_list[i + 1]))
            else:
                vector_list.append(self.__get_vector_length(point_list[0], point_list[i]))
            print(f'Длина вектора {i + 1} = {vector_list[i]}')
        print('----------------------------------------------------------')
        print(f'Периметр = {self.__get_perimeter(vector_list)}')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __get_vector_length(first: Point, second: Point) -> float:
        try:
            return round(math.sqrt((second.x - first.x) ** 2 + (second.y - first.y) ** 2), 2)
        except Exception as e:
            print(f'Ошибка: {e}')

    @staticmethod
    def __get_perimeter(vector_list: []) -> float:
        try:
            return sum(vector_list)
        except Exception as e:
            print(f'Ошибка: {e}')
