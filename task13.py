import re


class Task13:

    __task_number = 13

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        print('Дан символьный файл f. Группы символов, разделенные пробелами (одним или несколькими) и не'
              '\nсодержащие пробелов внутри себя, будем называть словами. Удалить из файла все однобуквенные слова'
              '\nи лишние пробелы. Результат записать в файл g. Переписать из файла g в файл h строки в'
              '\nперевернутом виде, порядок строк должен быть обратным')
        print('----------------------------------------------------------')
        text = self.__get_text()
        self.__do_task_a(text)
        print('----------------------------------------------------------')
        self.__do_task_b()
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    def __get_text(self) -> str:
        try:
            with open(f'files/inputs/task_{self.task_number}_input.txt') as f:
                return f.read()
        except Exception as e:
            print(f'Ошибка: {e}')

    def __do_task_a(self, text: str):
        try:
            changed_text = re.sub(r'\b(\w)\b', '', text)
            changed_text = re.sub(r'\s+', ' ', text)
            changed_text = re.sub(r'^\s|\s\.$|\s$', '', changed_text)
            self.__save_file(changed_text, 'a')
        except Exception as e:
            print(f'Ошибка: {e}')

    def __do_task_b(self):
        try:
            text = ''
            with open(f'files/outputs/task_{self.task_number}_output_a.txt') as f:
                text = f.read()
            self.__save_file(text[::-1], 'b')
        except Exception as e:
            print(f'Ошибка: {e}')

    def __save_file(self, text: [], task_variant: str):
        try:
            with open(f'files/outputs/task_{self.task_number}_output_{task_variant}.txt', "w") as output:
                output.write(text)
            print(f'{task_variant}) Файл сохранен как files/outputs/task_{self.task_number}_output_{task_variant}.txt')
        except Exception as e:
            print(f'Ошибка: {e}')
