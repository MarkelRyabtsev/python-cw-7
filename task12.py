import math

from helper import Helper, Point


class Task12:

    __task_number = 12

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Даны координаты вершин треугольника и координаты некоторой точки внутри него. Найти расстояние от '
              '\nданной точки до ближайшей стороны треугольника. (При определении расстояний учесть, что площадь '
              '\nтреугольника вычисляется и через три его стороны, и через основание и высоту.)')
        print('----------------------------------------------------------')
        a, b, c = self.__get_existing_triangle(helper)
        print(f'Треугольник: A({a.x}, {a.y}), B({b.x}, {b.y}), C({c.x}, {c.y})')
        m = self.__get_point_inside_triangle(helper, a, b, c)
        print(f'Точка внутри треугольника: M({m.x}, {m.y})')
        print('----------------------------------------------------------')
        ab_vector = self.__get_vector_length(a, b)
        ac_vector = self.__get_vector_length(a, c)
        bc_vector = self.__get_vector_length(b, c)
        area_amb = self.get_area(a, b, m)
        area_bmc = self.get_area(b, c, m)
        area_cma = self.get_area(c, a, m)
        height_ab = self.get_height(area_amb, ab_vector)
        height_bc = self.get_height(area_bmc, bc_vector)
        height_ac = self.get_height(area_cma, ac_vector)
        min_height = min(height_ab, height_bc, height_ac)
        if min_height == height_ab:
            print(f'Ближайшая сторона - AB, расстояние - {min_height}')
        elif min_height == height_bc:
            print(f'Ближайшая сторона - BC, расстояние - {min_height}')
        else:
            print(f'Ближайшая сторона - AC, расстояние - {min_height}')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def get_height(area: float, base_side: float) -> float:
        return round((2 * area) / base_side, 2)

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

    def __get_point_inside_triangle(self, helper: Helper, a: Point, b: Point, c: Point) -> Point:
        try:
            while True:
                m = helper.get_random_point()
                if self.__is_point_inside(a, b, c, m):
                    return m
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

    @staticmethod
    def __is_point_inside(a: Point, b: Point, c: Point, m: Point) -> bool:
        try:
            check_1 = (a.x - m.x) * (b.y - a.y) - (b.x - a.x) * (a.y - m.y)
            check_2 = (b.x - m.x) * (c.y - b.y) - (c.x - b.x) * (b.y - m.y)
            check_3 = (c.x - m.x) * (a.y - c.y) - (a.x - c.x) * (c.y - m.y)
            return (check_1 > 0 and check_2 > 0 and check_3 > 0) or (check_1 < 0 and check_2 < 0 and check_3 < 0)
        except Exception as e:
            print(f'Ошибка: {e}')
