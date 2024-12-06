import json


class Book:
    """Book object representation class."""

    def __init__(self, id: int, title: str, author: str,
                 year: int, status: str = 'В наличии') -> None:
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def get_json(self) -> dict:
        """Represent a book object in the json format."""
        data = {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'status': self.status
        }
        return data


class Library:
    """Library object representation class."""

    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        self.books = self.load_json(file_name)

    def create_json_file() -> None:
        with open('data.json', 'w', encoding='utf-8') as file:
            json.dump([], file, ensure_ascii=False, indent=4)

    def get_list_books(books: list) -> None:
        """Present a list of books in a readable form."""
        for book in books:
            print(f"ID: {book['id']}, Название: {book['title']}, "
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

    def get_id(self) -> int:
        """Get the last added book ID."""
        if self.books:
            id = self.books[-1].get('id', 0) + 1
        else:
            id = 0
        return id

    def add_book(self, new_book: Book) -> None:
        """Add a new book to the book list."""
        self.books.append(new_book)
        self.write_to_file(self.file_name)

    def delete_book(self, id: int) -> None:
        """Remove a book from the book list by ID."""
        for book in self.books:
            if book['id'] == id:
                self.books.remove(book)
                print('Книга удалена')
                self.write_to_file(self.file_name)
                break
        else:
            print('Книги с таким ID не существует')

    def update_status(self, id: int, status: str) -> None:
        """Change the status of a book."""
        for book in self.books:
            if book['id'] == id:
                book['status'] = status
                print(f'Статус книги изменен на "{status}".')
                self.write_to_file(self.file_name)
                break
        else:
            print('Книги с таким ID не существует')

    def find_title(self, title: str) -> list:
        """Search for a book by title."""
        find_list = []
        for book in self.books:
            if title in book['title']:
                find_list.append(book)
        if find_list:
            return find_list
        else:
            print('В библиотеке нет книг с таким названием')

    def find_author(self, author: str) -> list:
        """Search for a book by author."""
        find_list = []
        for book in self.books:
            if author in book['author']:
                find_list.append(book)
        if find_list:
            return find_list
        else:
            print('В библиотеке нет книг этого автора')

    def find_year(self, year: int) -> list:
        """Search for a book by year."""
        find_list = []
        for book in self.books:
            if year == book['year']:
                find_list.append(book)
        if find_list:
            return find_list
        else:
            print('В библиотеке нет книг этого года издания')
