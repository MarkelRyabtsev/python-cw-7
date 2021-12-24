from helper import Student


class Task1:
    __task_number = 1

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Сведения об ученике состоят из его имени и фамилии и названия класса (года обучения и буквы),'
              '\nв котором он учится. Дан типизированный  файл f, содержащий сведения об учениках школы:'
              '\n   а) выяснить, имеются ли в школе однофамильцы;'
              '\n   б) выяснить, имеются ли в школе однофамильцы, у которых совпадает и имя и фамилия;'  
              '\n   в) выяснить на сколько человек в восьмых классах больше, чем в десятых;'
              '\n   г) собрать в файле g сведения об учениках 9-х и 10-х классов, поместив вначале сведения об'
              '\nучениках класса 9а, затем 9б и т.д., затем 10а, 10б и т.д')
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
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __get_students() -> []:
        try:
            student_array = []
            with open('files/task_1_input.txt') as f:
                for line in f:
                    splitted_line = line.rsplit('\n')[0].split('|')
                    student_array.append(Student(
                        student_id=splitted_line[0],
                        first_name=splitted_line[1],
                        last_name=splitted_line[2],
                        class_number=splitted_line[3],
                        class_letter=splitted_line[4]
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
                    if student.student_id != s.student_id and student.last_name == s.last_name:
                        filtered_students_temp.append(student)
            print('а) Однофамильцы:')
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
                    if student.student_id != s.student_id and student.last_name == s.last_name and student.first_name == s.first_name:
                        filtered_students_temp.append(student)
            print('б) Однофамильцы, с одинаковыми именами:')
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
            filtered_students = [student for student in students if student.class_number == '8' or student.class_number == '10']
            count_eight_class = sum(student.class_number == '8' for student in filtered_students)
            count_ten_class = sum(student.class_number == '10' for student in filtered_students)
            if count_eight_class > count_ten_class:
                print(f'в) В 8 классах ({count_eight_class}) на {count_eight_class - count_ten_class} больше, чем в 10 ({count_ten_class})')
            elif count_ten_class > count_eight_class:
                print(f'в) В 10 классах ({count_ten_class}) на {count_ten_class - count_eight_class} больше, чем в 8 ({count_eight_class})')
            else:
                print(f'в) В 8 и 10 классах одинаковое кол-во человек: {count_eight_class}')
        except Exception as e:
            print(f'Ошибка: {e}')

    @staticmethod
    def __do_task_d(students: []):
        try:
            filtered_students_temp = [student for student in students if student.class_number == '9' or student.class_number == '10']
            filtered_students = sorted(filtered_students_temp, key=lambda x: (x.class_number, x.class_letter))
            with open('files/task_1_output.txt', "w") as output:
                for student in filtered_students:
                    output.write("".join(f'{student.student_id}|{student.first_name}|{student.last_name}|{student.class_number}|{student.class_letter}') + "\n")
            print('г) Файл сохранен как files/task_1_output.txt')
        except Exception as e:
            print(f'Ошибка: {e}')
