import collections
import json

from helper import Human


class Task16:
    __task_number = 16

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Дан типизированный файл f в который  вводятся имена, пол, возраст и рост человека. Программа'
              '\nсчитывает данные из файла и выдает совпадения'
              '\n   а) есть ли в нем мужчины одного роста;'
              '\n   б) женщины с одинаковыми именами;'
              '\n   в) мужчины и женщины одного возраста.'
              '\nПолученные данные записать в файл g')
        print('----------------------------------------------------------')
        humans = self.__get_humans()
        self.__do_task_a(humans)
        print('----------------------------------------------------------')
        self.__do_task_b(humans)
        print('----------------------------------------------------------')
        self.__do_task_c(humans)
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    def __get_humans(self) -> []:
        try:
            human_array = []
            with open(f'files/inputs/task_{self.task_number}_input.json') as f:
                data = json.load(f)
                for obj in data:
                    human_array.append(Human(
                        name=obj['name'],
                        gender=obj['gender'],
                        age=obj['age'],
                        height=obj['height']
                    ))
            return human_array
        except Exception as e:
            print(f'Ошибка: {e}')

    def __do_task_a(self, humans: []):
        try:
            male = []
            male_by_height = dict()
            for human in humans:
                if human.gender == 'Male':
                    male.append(human)
            for m in male:
                if m.height in male_by_height.keys():
                    male_by_height[m.height] = male_by_height[m.height] + 1
                else:
                    male_by_height[m.height] = 1
            male_by_height_filtered = dict(
                sorted({height: count for height, count in male_by_height.items() if count > 1}.items()))
            if len(male_by_height_filtered) > 0:
                with open(f'files/outputs/task_{self.task_number}_a_output.txt', "w") as output:
                    for (height, count) in male_by_height_filtered.items():
                        output.write("".join(f'Рост: {height}') + f', кол-во: {count}' + "\n")
                print(f'Файл сохранен как files/outputs/task_{self.task_number}_a_output.txt')
            else:
                print('Мужчин одного роста нет.')
        except Exception as e:
            print(f'Ошибка: {e}')

    def __do_task_b(self, humans: []):
        try:
            female = []
            female_by_name = dict()
            for human in humans:
                if human.gender == 'Female':
                    female.append(human)
            for f in female:
                if f.name in female_by_name.keys():
                    female_by_name[f.name] = female_by_name[f.name] + 1
                else:
                    female_by_name[f.name] = 1
            female_by_name_filtered = dict(
                sorted({name: count for name, count in female_by_name.items() if count > 1}.items()))
            if len(female_by_name_filtered) > 0:
                with open(f'files/outputs/task_{self.task_number}_b_output.txt', "w") as output:
                    for (name, count) in female_by_name_filtered.items():
                        output.write("".join(f'Имя: {name}') + f', кол-во: {count}' + "\n")
                print(f'Файл сохранен как files/outputs/task_{self.task_number}_b_output.txt')
            else:
                print('Женщин с одним именем нет.')
        except Exception as e:
            print(f'Ошибка: {e}')

    def __do_task_c(self, humans: []):
        try:
            humans_by_height = dict()
            for h in humans:
                if h.height in humans_by_height.keys():
                    humans_by_height[h.height] = (
                    humans_by_height[h.height][0] + 1, humans_by_height[h.height][1]) if h.gender == 'Male' else (
                    humans_by_height[h.height][0], humans_by_height[h.height][1] + 1)
                else:
                    humans_by_height[h.height] = (1, 0) if h.gender == 'Male' else (0, 1)
            humans_by_height_filtered = dict(
                sorted({height: (m_count, f_count) for height, (m_count, f_count) in humans_by_height.items() if m_count > 1 or f_count > 1}.items()))
            if len(humans_by_height_filtered) > 0:
                with open(f'files/outputs/task_{self.task_number}_c_output.txt', "w") as output:
                    for (height, (m_count, f_count)) in humans_by_height_filtered.items():
                        output.write("".join(f'Имя: {height}') + f', мужчин: {m_count}' + f', женщин {f_count}' + "\n")
                print(f'Файл сохранен как files/outputs/task_{self.task_number}_c_output.txt')
            else:
                print('Нет мужчин и женщин с одинаковым ростом.')
        except Exception as e:
            print(f'Ошибка: {e}')
