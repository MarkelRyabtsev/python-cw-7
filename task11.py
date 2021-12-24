import math
from helper import Helper, Point


class Task11:

    __task_number = 11

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Даны координаты вершин двух треугольников. Определить, какой из них имеет большую площадь')
        print('----------------------------------------------------------')
        a_1, b_1, c_1 = self.__get_existing_triangle(helper)
        a_2, b_2, c_2 = self.__get_existing_triangle(helper)
        print(f'Треугольник 1: A1({a_1.x}, {a_1.y}), B1({b_1.x}, {b_1.y}), C1({c_1.x}, {c_1.y})')
        print(f'Треугольник 2: A2({a_2.x}, {a_2.y}), B2({b_2.x}, {b_2.y}), C2({c_2.x}, {c_2.y})')
        print('----------------------------------------------------------')
        area_1 = self.get_area(a_1, b_1, c_1)
        area_2 = self.get_area(a_2, b_2, c_2)
        symbol = ''
        if area_1 > area_2:
            symbol = '>'
        elif area_1 < area_2:
            symbol = '<'
        else:
            symbol = '='
        print(f"Площадь Треугольника 1 ({area_1}) {symbol} {'Треугольника' if symbol != '=' else 'Треугольнику'} 2 ({area_2})")
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    def get_area(self, a: Point, b: Point, c: Point) -> float:
        ab = self.__get_vector_length(a, b)
        bc = self.__get_vector_length(b, c)
        ac = self.__get_vector_length(a, c)
        half_p = (ab + bc + ac) / 2
        area = math.sqrt(half_p * (half_p - ab) * (half_p - bc) * (half_p - ac))
        return round(area, 2)

    def __get_existing_triangle(self, helper: Helper) -> tuple[Point, Point, Point]:
        try:
            while True:
                a = helper.get_random_point()
                b = helper.get_random_point()
                c = helper.get_random_point()
                if self.__is_exist(
                        self.__get_vector_length(a, b),
                        self.__get_vector_length(a, c),
                        self.__get_vector_length(b, c)
                ):
                    return a, b, c
        except Exception as e:
            print(f'Ошибка: {e}')

    @staticmethod
    def __get_vector_length(point_1: Point, point_2: Point) -> float:
        return abs(round(math.sqrt((point_2.x - point_1.x) ** 2 + (point_2.y - point_1.y) ** 2), 2))

    @staticmethod
    def __is_exist(x: float, y: float, z: float) -> bool:
        try:
            return x < y + z and y < x + z and z < x + y
        except Exception as e:
            print(f'Ошибка: {e}')
