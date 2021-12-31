import json

from helper import Book, Helper


class Task10:
    __task_number = 10

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Дан типизированный файл f, содержащий сведения о книгах. Сведения о каждой из книг - это фамилия'
              '\nавтора, название и год издания.'
              '\n   1) Найти названия книг данного автора, изданных с 1960 г.'
              '\n   2) Определить, имеется ли книга с названием "Программирование на Pascal". Если да, то сообщить '
              '\nфамилию автора и год издания. Если таких книг несколько, то сообщить имеющиеся сведения '
              '\nобо всех книгах')
        print('----------------------------------------------------------')
        books = self.__get_books()
        self.__do_task_a(books, helper)
        print('----------------------------------------------------------')
        self.__do_task_b(books, 'Программирование на Pascal')
        self.__do_task_b(books, 'Неизвестность')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    def __get_books(self) -> []:
        try:
            book_array = []
            with open(f'files/inputs/task_{self.task_number}_input.json', encoding="utf-8") as f:
                data = json.load(f)
                for obj in data:
                    book_array.append(Book(
                        name=obj['Name'],
                        author=obj['Author'],
                        year=obj['PubYear']
                    ))
            return book_array
        except Exception as e:
            print(f'Ошибка: {e}')

    @staticmethod
    def __do_task_a(books: [], helper: Helper):
        try:
            authors_dict = dict()
            number_author = 1
            for book in books:
                if book.author not in authors_dict.keys():
                    authors_dict[book.author] = number_author
                    number_author += 1
            print('а) Введите номер автора:')
            for (author, number) in authors_dict.items():
                print(f'{number}) {author}')
            number = helper.set_natural_number('Введите номер автора:', range(1, number_author), False)
            books_by_author = [book_by_author for book_by_author in books
                               if authors_dict[book_by_author.author] == number
                               and book_by_author.year > 1960]
            print(f'Книги автора {books_by_author[0].author}:')
            for book in books_by_author:
                print(f'{book.name} - {book.year}')
        except Exception as e:
            print(f'Ошибка: {e}')

    @staticmethod
    def __do_task_b(books: [], book_name: str):
        try:
            books_by_name = [book for book in books if book.name == book_name]
            if len(books_by_name) > 0:
                for book in books_by_name:
                    print(f'{book.name} - {book.author} - {book.year}')
            else:
                print(f'Книга "{book_name}" в списке отсутствует')
        except Exception as e:
            print(f'Ошибка: {e}')
