from datetime import datetime


class Task6:

    __task_number = 6

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Дан типизированный файл f, содержащий различные даты. Каждая дата - это число, месяц и год. Найти: '
              '\n   а) год с наименьшим номером;'
              '\n   б) все весенние даты;'
              '\n   в) самую позднюю дату.'
              'Найденные данные записать в файл g')
        print('----------------------------------------------------------')
        dates = self.__get_dates()
        self.__do_task_a(dates)
        self.__do_task_b(dates)
        self.__do_task_c(dates)
        print(f'Файл сохранен как files/outputs/task_{self.task_number}_output.txt')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    def __get_dates(self) -> []:
        try:
            dates_array = [datetime]
            with open(f'files/inputs/task_{self.task_number}_input.txt') as f:
                for line in f:
                    date_line = line.split('\n')[0]
                    dates_array.append(datetime.strptime(date_line, '%d/%m/%Y'))
            return dates_array
        except Exception as e:
            print(f'Ошибка: {e}')

    def __do_task_a(self, dates: [datetime]):
        try:
            min_year = min([date.year for date in dates][2:])
            text_to_append = f'а) Год с наименьшим номером - {min_year}\n'
            self.__append_to_file(text_to_append)
        except Exception as e:
            print(f'Ошибка: {e}')

    def __do_task_b(self, dates: [datetime]):
        try:
            spring_dates = [date for date in dates if date.month in [3, 4, 5]][2:]
            text_to_append = f'б) Все весенние даты:\n'
            for date in spring_dates:
                text_to_append = text_to_append + f'{date.day}/{date.month}/{date.year}\n'
            self.__append_to_file(text_to_append)
        except Exception as e:
            print(f'Ошибка: {e}')

    def __do_task_c(self, dates: [datetime]):
        try:
            max_date = max(dates[2:])
            text_to_append = f'в) Самая поздняя дата - {max_date.day}/{max_date.month}/{max_date.year}'
            self.__append_to_file(text_to_append)
        except Exception as e:
            print(f'Ошибка: {e}')

    def __append_to_file(self, text_to_append: str):
        try:
            with open(f'files/outputs/task_{self.task_number}_output.txt', 'a') as output:
                output.write(text_to_append)
        except Exception as e:
            print(f'Ошибка: {e}')
