import random


class Student:

    def __init__(self, student_id, first_name, last_name, class_number, class_letter, grades=None):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.class_number = class_number
        self.class_letter = class_letter
        self.grades = grades


class Cube:

    def __init__(self, edge, color, material):
        self.edge = edge
        self.color = color
        self.material = material


class Book:

    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year


class Car:

    def __init__(self, car_model, car_number, owner):
        self.car_model = car_model
        self.car_number = car_number
        self.owner = owner


class Human:

    def __init__(self, name, gender, age, height):
        self.name = name
        self.gender = gender
        self.age = age
        self.height = height


class Helper:

    @staticmethod
    def set_natural_number(description: str, numbers_range: range = None, all_numbers: bool = False) -> int:
        while True:
            try:
                value = int(input(f'{description} : '))
                if not all_numbers:
                    if value < 1:
                        print('Число должно быть больше 0!')
                        continue
                if numbers_range is not None and value not in numbers_range:
                    print(f'Введенное число должно быть в диапозоне от {numbers_range.start} до {numbers_range.stop}!')
                    continue
                return value
            except:
                print('Введенное значение не является натуральным числом, повторите!')
                continue
