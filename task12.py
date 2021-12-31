import json
from helper import Helper, Car


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
        print('Сведения об автомобиле состоят из его марки, номера и фамилии владельца. Дан типизированный'
              '\nфайл f, содержащий сведения о нескольких автомобилях. Найти:'
              '\n   а) фамилии владельцев и номера автомобилей данной марки;'
              '\n   б) количество автомобилей каждой марки.'
              'Найденные данные записать в файл g')
        print('----------------------------------------------------------')
        cars = self.__get_cars()
        self.__do_task_a(cars, helper)
        print('----------------------------------------------------------')
        self.__do_task_b(cars)
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    def __get_cars(self) -> []:
        try:
            car_array = []
            with open(f'files/inputs/task_{self.task_number}_input.json') as f:
                data = json.load(f)
                for obj in data:
                    car_array.append(Car(
                        car_model=obj['car_model'],
                        car_number=obj['car_number'],
                        owner=obj['owner']
                    ))
            return car_array
        except Exception as e:
            print(f'Ошибка: {e}')

    def __do_task_a(self, cars: [], helper: Helper):
        try:
            cars_dict = dict()
            number_car = 1
            for car in cars:
                if car.car_model not in cars_dict.keys():
                    cars_dict[car.car_model] = number_car
                    number_car += 1
            print('а) Введите номер марки:')
            for (model, number) in cars_dict.items():
                print(f'{number}) {model}')
            number = helper.set_natural_number('Введите номер марки:', range(1, number_car), False)
            cars_by_model = [car_by_model for car_by_model in cars
                               if cars_dict[car_by_model.car_model] == number]
            with open(f'files/outputs/task_{self.task_number}_a_{cars_by_model[0].car_model}_output.txt', "w") as output:
                for car in cars_by_model:
                    output.write("".join(
                        f'Владелец: {car.owner}') + f', номер: {car.car_number}' + "\n")
            print(f'Файл сохранен как files/outputs/task_{self.task_number}_a_{cars_by_model[0].car_model}_output.txt')
        except Exception as e:
            print(f'Ошибка: {e}')

    def __do_task_b(self, cars: []):
        try:
            cars_dict = dict()
            for car in cars:
                if car.car_model in cars_dict.keys():
                    cars_dict[car.car_model] = cars_dict[car.car_model] + 1
                else:
                    cars_dict[car.car_model] = 1
            with open(f'files/outputs/task_{self.task_number}_b_output.txt', "w") as output:
                for (model, count) in cars_dict.items():
                    output.write("".join(
                        f'Марка: {model}') + f', количество: {count}' + "\n")
            print(f'б) Файл сохранен как files/outputs/task_{self.task_number}_b_output.txt')
        except Exception as e:
            print(f'Ошибка: {e}')
