import json
from helper import Student


class Task8:

    __task_number = 8

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Сведения об ученике состоят из его имени и фамилии и названия класса (года обучения и буквы),'
              '\nв котором он учится. Дан типизированный  файл f, содержащий сведения об учениках школы:'
              '\n   а) выяснить, имеются ли однофамильцы в каких-либо параллельных классах;'
              '\n   б) выяснить, имеются ли однофамильцы в каком-нибудь классе;'
              '\n   в) выяснить, имеются ли однофамильцы в каких-либо параллельных классах у которых'
              '\nсовпадает и имя и фамилия;' 
              '\n   г) выяснить, имеются ли однофамильцы в каком-нибудь классе, у которых совпадает и имя и фамилия;'
              '\n   д) выяснить, в каких классах насчитывается более 35 учащихся;')
        print('----------------------------------------------------------')
        students = self.__get_students()
        print('----------------------------------------------------------')
        self.__do_task_a(students)
        print('----------------------------------------------------------')
        self.__do_task_b(students)
        print('----------------------------------------------------------')
        self.__do_task_c(students)
        print('----------------------------------------------------------')
        self.__do_task_d(students)
        print('----------------------------------------------------------')
        self.__do_task_e(students)
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    def __get_students(self) -> []:
        try:
            student_array = []
            with open(f'files/inputs/task_{self.task_number}_input.json') as f:
                data = json.load(f)
                for obj in data:
                    student_array.append(Student(
                        student_id=obj['id'],
                        first_name=obj['first_name'],
                        last_name=obj['last_name'],
                        class_number=obj['class_number'],
                        class_letter=obj['class_letter']
                    ))
            return student_array
        except Exception as e:
            print(f'Ошибка: {e}')

    @staticmethod
    def __do_task_a(students: []):
        try:
            filtered_students_temp = []
            filtered_students = []
            for student in students:
                for s in students:
                    if student.student_id != s.student_id \
                            and student.last_name == s.last_name\
                            and student.class_number == s.class_number\
                            and student.class_letter != s.class_letter:
                        filtered_students_temp.append(student)
            print('а) Однофамильцы в паралельных классах:')
            if len(filtered_students_temp) > 0:
                filtered_students = sorted(filtered_students_temp, key=lambda x: (x.last_name, x.first_name))
                for student in filtered_students:
                    print(f'{student.first_name} {student.last_name} из {student.class_number}{student.class_letter}')
            else:
                print('Отсутствуют.')
        except Exception as e:
            print(f'Ошибка: {e}')

    @staticmethod
    def __do_task_b(students: []):
        try:
            filtered_students_temp = []
            filtered_students = []
            for student in students:
                for s in students:
                    if student.student_id != s.student_id \
                            and student.last_name == s.last_name \
                            and student.class_number == s.class_number\
                            and student.class_letter == s.class_letter:
                        filtered_students_temp.append(student)
            print('б) Однофамильцы в классах:')
            if len(filtered_students_temp) > 0:
                filtered_students = sorted(filtered_students_temp, key=lambda x: x.last_name)
                for student in filtered_students:
                    print(f'{student.first_name} {student.last_name} из {student.class_number}{student.class_letter}')
            else:
                print('Отсутствуют.')
        except Exception as e:
            print(f'Ошибка: {e}')

    @staticmethod
    def __do_task_c(students: []):
        try:
            filtered_students_temp = []
            filtered_students = []
            for student in students:
                for s in students:
                    if student.student_id != s.student_id \
                            and student.last_name == s.last_name \
                            and student.first_name == s.first_name\
                            and student.class_number == s.class_number\
                            and student.class_letter != s.class_letter:
                        filtered_students_temp.append(student)
            print('в) Полные однофамильцы в паралельных классах:')
            if len(filtered_students_temp) > 0:
                filtered_students = sorted(filtered_students_temp, key=lambda x: x.last_name)
                for student in filtered_students:
                    print(f'{student.first_name} {student.last_name} из {student.class_number}{student.class_letter}')
            else:
                print('Отсутствуют.')
        except Exception as e:
            print(f'Ошибка: {e}')

    @staticmethod
    def __do_task_d(students: []):
        try:
            filtered_students_temp = []
            filtered_students = []
            for student in students:
                for s in students:
                    if student.student_id != s.student_id \
                            and student.last_name == s.last_name \
                            and student.first_name == s.first_name\
                            and student.class_number == s.class_number\
                            and student.class_letter == s.class_letter:
                        filtered_students_temp.append(student)
            print('г) Полные однофамильцы в паралельных классах:')
            if len(filtered_students_temp) > 0:
                filtered_students = sorted(filtered_students_temp, key=lambda x: x.last_name)
                for student in filtered_students:
                    print(f'{student.first_name} {student.last_name} из {student.class_number}{student.class_letter}')
            else:
                print('Отсутствуют.')
        except Exception as e:
            print(f'Ошибка: {e}')

    @staticmethod
    def __do_task_e(students: []):
        try:
            classes_dict = dict()
            for student in students:
                if (student.class_number, student.class_letter) in classes_dict.keys():
                    classes_dict[(student.class_number, student.class_letter)] = \
                        classes_dict[(student.class_number, student.class_letter)] + 1
                else:
                    classes_dict[(student.class_number, student.class_letter)] = 0
            print('д) Классы с кол-ом учеников больше 35:')
            if len([key for key in classes_dict.keys() if classes_dict[key] > 35]) == 0:
                print('Отсутствуют.')
            else:
                for (key, value) in classes_dict.items():
                    if value > 35:
                        print(f'{key[0]}{key[1]} - {classes_dict[key]}')
        except Exception as e:
            print(f'Ошибка: {e}')
