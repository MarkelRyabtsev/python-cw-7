import json
from helper import Cube


class Task4:
    __task_number = 4

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Дан типизированный файл f, содержащий сведения о кубиках: размер каждого кубика (длина ребра'
              '\nв сантиметрах), его цвет (красный, зеленый, желтый или синий) и материал (деревянный,'
              '\nметаллический, картонный). Найти: '
              '\n   а) количество кубиков каждого из перечисленных цветов и их суммарный объем;'
              '\n   б) количество деревянных кубиков с ребром 3 см и количество металлических кубиков с ребром, большим 5 см')
        print('----------------------------------------------------------')
        cubes = self.__get_cubes()
        self.__do_task_a(cubes)
        print('----------------------------------------------------------')
        self.__do_task_b(cubes)
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    def __get_cubes(self) -> [Cube]:
        try:
            cubes_array = []
            with open(f'files/inputs/task_{self.task_number}_input.json') as f:
                data = json.load(f)
                for obj in data:
                    cubes_array.append(Cube(
                        edge=obj['edge'],
                        color=obj['color'],
                        material=obj['material']
                    ))
            return cubes_array
        except Exception as e:
            print(f'Ошибка: {e}')

    @staticmethod
    def __do_task_a(cubes: [Cube]):
        try:
            colors_dict = dict()
            for cube in cubes:
                if cube.color in colors_dict.keys():
                    colors_dict[cube.color] = [colors_dict[cube.color][0] + 1,
                                               colors_dict[cube.color][1] + cube.edge ** 3]
                else:
                    colors_dict[cube.color] = [0, 0]
            for color in colors_dict.keys():
                print(f'{color}: кол-во - {colors_dict[color][0]}, общий объем - {colors_dict[color][1]}')
        except Exception as e:
            print(f'Ошибка: {e}')

    @staticmethod
    def __do_task_b(cubes: [Cube]):
        try:
            cubes_dict = dict()
            filtered_cubes = [cube for cube in cubes if cube.material == 'wood' or cube.material == 'metal']
            for cube in filtered_cubes:
                if cube.material in cubes_dict.keys():
                    if (cube.material == 'wood' and cube.edge == 3) or (cube.material == 'metal' and cube.edge > 5):
                        cubes_dict[cube.material] = cubes_dict[cube.material] + 1
                else:
                    cubes_dict[cube.material] = 0
            for material in cubes_dict.keys():
                print(f'{material}: кол-во - {cubes_dict[material]}')
        except Exception as e:
            print(f'Ошибка: {e}')
