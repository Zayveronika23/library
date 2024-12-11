import os

from app.handlers import (choose_action, handle_add_new_book,
                          handle_delete_book, handle_find_book,
                          handle_get_books, handle_update_book)
from app.models.library import Library

library = Library()


def main(FILE_NAME='data.json') -> None:
    """Start function for selecting, entering values and calling methods."""
    try:
        if not os.path.exists(FILE_NAME):
            Library.create_json_file()
        while True:
            action = choose_action()
            match action:
                case 'g':
                    handle_get_books(library)
                case 'a':
                    handle_add_new_book(library)
                case 'u':
                    handle_update_book(library)
                case 'd':
                    handle_delete_book(library)
                case 'f':
                    handle_find_book(library)
                case 'x':
                    exit()
                case _:
                    print('Такого действия не существует')
            break
    except KeyboardInterrupt:
        print('\nДо скорых встреч!')


if __name__ == "__main__":
    main()
