import abc

from app.models.book import Book
from app.models.library import Library


class InputPort(abc.ABC):
    """Абстрактный базовый класс для ввода данных."""

    @abc.abstractmethod
    def get_year_from_user(
            self, prompt: str = 'Введите год издания книги: ') -> int:
        pass

    def get_book_id_from_user(
            self, prompt: str = 'Введите номер книги: ') -> int:
        pass

    def get_title_from_user(
            self, prompt: str = 'Введите название книги: ') -> str:
        pass

    def get_author_from_user(
            self, prompt: str = 'Введите автора  книги: ') -> str:
        pass

    def get_action_from_user(self, prompt: str = '') -> str:
        pass


class ConsoleInputPort(InputPort):

    def get_year_from_user(
            self, prompt: str = 'Введите год издания книги: ') -> int:
        value = int(input(prompt))
        return value

    def get_book_id_from_user(
            self, prompt: str = 'Введите номер книги: ') -> int:
        value = int(input(prompt))
        return value

    def get_title_from_user(
            self, prompt: str = 'Введите название книги: ') -> str:
        value = input(prompt)
        return value

    def get_author_from_user(
            self, prompt: str = 'Введите автора книги: ') -> str:
        value = input(prompt)
        return value

    def get_action_from_user(self, prompt: str = '') -> str:
        value = input(prompt)
        return value.lower()


input_port = ConsoleInputPort()


def choose_action() -> str:
    action = input_port.get_action_from_user(
                '''Выберите действие:
                Добавить книгу(А),
                Посмотреть все книги(G),
                Изменить наличие книги(U),
                Удалить книгу(D),
                Поиск книги(F),
                Закрыть программу(X): ''')
    return action


def handle_get_books(library: Library) -> None:
    books = library.get_books()
    if books:
        Library.get_list_books(books)
    else:
        print(books)
        print('В библиотеке еще нет книг')


def handle_add_new_book(library: Library) -> None:
    book_id = library.get_book_id()
    title = input_port.get_title_from_user()
    author = input_port.get_author_from_user()
    try:
        year = input_port.get_year_from_user()
    except ValueError:
        print('Введите год в числовом формате.')
    else:
        book = Book(title, author, year)
        book.add_book_id(book_id)
        book = book.get_json()
        library.add_book(book)
        print('Книга успешно добавлена!')


def handle_update_book(library: Library) -> None:
    try:
        book_id = input_port.get_book_id_from_user()
    except ValueError:
        print('Введите ID в числовом формате.')
    else:
        status = input_port.get_action_from_user(
            'Введите статус книги: В наличии(Y), Выдана(N)')
        if status == 'y':
            status = 'В наличии'
        elif status == 'n':
            status = 'Выдана'
        else:
            print('Такого статуса не предусмотрено')
        library.update_status(book_id, status)


def handle_delete_book(library: Library) -> None:
    try:
        book_id = input_port.get_book_id_from_user()
    except ValueError:
        print('Введите ID в числовом формате.')
    else:
        library.delete_book(book_id)


def handle_find_book(library: Library) -> None:
    tag = input_port.get_action_from_user(
            '''Поиск можно совершить по названию(T),
            по автору(A), по году(Y): ''')
    tag = tag.lower()
    match tag:
        case't':
            title = input_port.get_title_from_user()
            books = library.find_title(title)
            if books:
                Library.get_list_books(books)
        case 'a':
            author = input_port.get_title_from_user()
            books = library.find_author(author)
            if books:
                Library.get_list_books(books)
        case 'y':
            try:
                year = input_port.get_year_from_user()
            except ValueError:
                print('Введите год в числовом формате.')
            else:
                books = library.find_year(year)
                if books:
                    Library.get_list_books(books)
        case _:
            print('Такого поиска не предусмотрено')
