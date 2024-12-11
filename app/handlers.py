from app.models.book import Book
from app.models.library import Library


def choose_action() -> str:
    action = input(
                '''Выберите действие:
                Добавить книгу(А),
                Посмотреть все книги(G),
                Изменить наличие книги(U),
                Удалить книгу(D),
                Поиск книги(F),
                Закрыть программу(X): ''')
    action = action.lower()
    return action


def handle_get_books(library: Library) -> None:
    books = library.books
    if books:
        Library.get_list_books(books)
    else:
        print('В библиотеке еще нет книг')


def handle_add_new_book(library: Library) -> None:
    book_id = library.get_book_id()
    title = input('Введите название книги: ')
    author = input('Введите автора книги: ')
    try:
        year = int(input('Введите год издания книги: '))
        book = Book(title, author, year)
        book.add_book_id(book_id)
        book = book.get_json()
        library.add_book(book)
    except ValueError:
        print('Введите год в числовом формате.')
    else:
        print('Книга успешно добавлена')


def handle_update_book(library: Library) -> None:
    try:
        book_id = int(input('Введите номер книги: '))
    except ValueError:
        print('Введите ID в числовом формате.')
    else:
        status = input('Введите статус книги: В наличии(Y), Выдана(N)')
        if status.lower() == 'y':
            status = 'В наличии'
        elif status.lower() == 'n':
            status = 'Выдана'
        else:
            print('Такого статуса не предусмотрено')
            return
        library.update_status(book_id, status)


def handle_delete_book(library: Library) -> None:
    try:
        book_id = int(input('Введите номер книги: '))
        library.delete_book(book_id)
    except ValueError:
        print('Введите ID в числовом формате.')


def handle_find_book(library: Library) -> None:
    tag = input('''Поиск можно совершить по названию(T), '
                'по автору(A), по году(Y): ''')
    tag = tag.lower()
    match tag:
        case't':
            title = input('Введите название книги: ')
            books = library.find_title(title)
            if books:
                Library.get_list_books(books)
        case 'a':
            author = input('Введите автора книги: ')
            books = library.find_author(author)
            if books:
                Library.get_list_books(books)
        case 'y':
            try:
                year = int(input('Введите год издания книги: '))
                books = library.find_year(year)
                if books:
                    Library.get_list_books(books)
            except ValueError:
                print('Введите год в числовом формате.')
        case _:
            print('Такого поиска не предусмотрено')
