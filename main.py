import os

from library import Book, Library


def main() -> None:
    if not os.path.exists('data.json'):
        Library.create_json_file()
    """Start function for selecting, entering values ​​and calling methods."""
    while True:
        action = input('Выберите действие: Добавить книгу(А), '
                       'Посмотреть все книги(G), Изменить наличие книги(U), '
                       'Удалить книгу(D), Поиск книги(F), '
                       'Закрыть программу(X): ')
        action = action.lower()
        library = Library('data.json')
        if action == 'g':
            books = library.books
            if books:
                Library.get_list_books(books)
            else:
                print('В библиотеке еще нет книг')

        elif action == 'a':
            id = library.get_id()
            title = input('Введите название книги: ')
            author = input('Введите автора книги: ')
            try:
                year = int(input('Введите год издания книги: '))
                book = Book(id, title, author, year)
                book = book.get_json()
                library.add_book(book)
            except ValueError:
                print('Введите год в числовом формате.')
            else:
                print('Книга успешно добавлена')

        elif action == 'u':
            try:
                id = int(input('Введите номер книги: '))
                status = input('Введите статус книги: В наличии(Y), Выдана(N)')
                if status.lower() == 'y':
                    status = 'В наличии'
                elif status.lower() == 'n':
                    status = 'Выдана'
                else:
                    print('Такого статуса не предусмотрено')
                    continue
                library.update_status(id, status)
            except ValueError:
                print('Введите ID в числовом формате.')

        elif action == 'd':
            try:
                id = int(input('Введите номер книги: '))
                library.delete_book(id)
            except ValueError:
                print('Введите ID в числовом формате.')

        elif action == 'f':
            tag = (input('Поиск можно совершить по названию(T), '
                         'по автору(A), по году(Y): '))
            tag = tag.lower()
            if tag == 't':
                title = input('Введите название книги: ')
                books = library.find_title(title)
                if books:
                    Library.get_list_books(books)
            elif tag == 'a':
                author = input('Введите автора книги: ')
                books = library.find_author(author)
                if books:
                    Library.get_list_books(books)
            elif tag == 'y':
                try:
                    year = int(input('Введите год издания книги: '))
                    books = library.find_year(year)
                    if books:
                        Library.get_list_books(books)
                except ValueError:
                    print('Введите год в числовом формате.')
            else:
                print('Такого поиска не предусмотрено')

        elif action == 'x':
            exit()
        else:
            print('Такого действия не существует')


if __name__ == "__main__":
    main()
