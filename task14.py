import json
from helper import Helper, Student


class Task14:

    __task_number = 14

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Сведения об ученике состоят из его имени и фамилии, названия класса (года обучения и буквы), в'
              '\nкотором он учится и отметки. Дан типизированный  файл f, содержащий сведения об учениках школы:'
              '\n   а) выяснить, сколько учеников школы не имеют отметок ниже четырех;'
              '\n   б) собрать в файле g сведения о лучших учениках школы, т.е. об учениках, не имеющих отметок'
              '\nниже четырех и по сумме баллов не уступающих другим ученикам своего и параллельных классов')
        print('----------------------------------------------------------')
        students = self.__get_students()
        self.__do_task(students)
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
                        class_letter=obj['class_letter'],
                        grades=obj['grades']
                    ))
            return student_array
        except Exception as e:
            print(f'Ошибка: {e}')

    def __do_task(self, students: []):
        try:
            filtered_students = []
            for student in students:
                if all(int(grade) >= 4 for grade in student.grades):
                    filtered_students.append(student)
            print(f'а) Количество учеников не имеющих оценки, ниже 4: {len(filtered_students)}')
            self.__save_file(filtered_students)
        except Exception as e:
            print(f'Ошибка: {e}')

    def __save_file(self, students: []):
        try:
            with open(f'files/outputs/task_{self.task_number}_output_b.txt', "w") as output:
                for student in students:
                    output.write("".join(
                        f'{student.student_id}|{student.first_name}|{student.last_name}|{student.class_number}|{student.class_letter}')
                                 + "\n")
            print(f'б) Список лучших учеников сохранен как files/outputs/task_{self.task_number}_output_b.txt')
        except Exception as e:
            print(f'Ошибка: {e}')
