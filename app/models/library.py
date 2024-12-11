import json
from typing import Optional

from app.models.book import Book


class Library:
    """Library object representation class."""

    def __init__(self, file_name: str = 'data.json') -> None:
        self.file_name = file_name
        self.books = self.load_json(file_name)

    def create_json_file(filename='data.json') -> None:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump([], file, ensure_ascii=False, indent=4)

    def get_list_books(books: list) -> None:
        """Present a list of books in a readable form."""
        for book in books:
            print(f"ID: {book['book_id']}, Название: {book['title']}, "
                  f"Автор: {book['author']}, Год издания: {book['year']}, "
                  f"Статус: {book['status']}")

    def load_json(self, file_name: str) -> list:
        """Load a list of books from a file."""
        with open(file_name, 'r', encoding='utf-8') as file:
            loaded_data = json.load(file)
        return loaded_data

    def write_to_file(self, file_name: str) -> None:
        """Load a list of books into a file."""
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(self.books, file, ensure_ascii=False, indent=4)

    def get_book_id(self) -> int:
        """Get the last added book ID."""
        if self.books:
            book_id = self.books[-1].get('book_id', 0) + 1
        else:
            book_id = 0
        return book_id

    def add_book(self, new_book: Book) -> None:
        """Add a new book to the book list."""
        self.books.append(new_book)
        self.write_to_file(self.file_name)

    def delete_book(self, book_id: int) -> None:
        """Remove a book from the book list by ID."""
        for book in self.books:
            if book['book_id'] == book_id:
                self.books.remove(book)
                print('Книга удалена')
                self.write_to_file(self.file_name)
                break
        else:
            print('Книги с таким ID не существует')

    def update_status(self, book_id: int, status: str) -> None:
        """Change the status of a book."""
        for book in self.books:
            if book['book_id'] == book_id:
                book['status'] = status
                print(f'Статус книги изменен на "{status}".')
                self.write_to_file(self.file_name)
                break
        else:
            print('Книги с таким ID не существует')

    def find_title(self, title: str) -> Optional[list]:
        """Search for a book by title."""
        find_list = []
        for book in self.books:
            if title in book['title']:
                find_list.append(book)
        if find_list:
            return find_list
        else:
            print('В библиотеке нет книг с таким названием')

    def find_author(self, author: str) -> Optional[list]:
        """Search for a book by author."""
        find_list = []
        for book in self.books:
            if author in book['author']:
                find_list.append(book)
        if find_list:
            return find_list
        else:
            print('В библиотеке нет книг этого автора')

    def find_year(self, year: int) -> Optional[list]:
        """Search for a book by year."""
        find_list = []
        for book in self.books:
            if year == book['year']:
                find_list.append(book)
        if find_list:
            return find_list
        else:
            print('В библиотеке нет книг этого года издания')
