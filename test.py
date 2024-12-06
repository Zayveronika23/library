import json
import os
import unittest

from library import Book, Library


class TestBook(unittest.TestCase):
    """Сhecks the methods of the book class."""

    def test_create_book(self):
        """Сhecks the creation of an object of the book class"""
        book = Book(0, 'title', 'author', 1900)
        self.assertEqual(book.status, 'В наличии')


class TestLibrary(unittest.TestCase):
    """Сhecks the methods of the library class."""

    def setUp(self):
        test_data = [
            {
                "id": 0,
                "title": "first_title",
                "author": "first_author",
                "year": 1900,
                "status": "В наличии"
            },
            {
                "id": 1,
                "title": "second_title",
                "author": "second_author",
                "year": 1901,
                "status": "Выдана"
            }]
        with open('test_data.json', 'w', encoding='utf-8') as file:
            json.dump(test_data, file, ensure_ascii=False, indent=4)
        self.library = Library('test_data.json')

    def tearDown(self):
        os.remove('test_data.json')

    def test_get_all_book(self):
        """Checks the function to get all books."""
        amount_books = len(self.library.books)
        self.assertEqual(amount_books, 2)

    def test_add_new_book(self):
        """Checks the function to add new book."""
        new_book = Book(2, 'third_title', 'third_author', 1902)
        new_book = new_book.get_json()
        self.library.add_book(new_book)
        new_amount_book = len(self.library.books)
        self.assertEqual(new_amount_book, 3)

    def test_get_id(self):
        """Checks the function to get last ID."""
        new_id = self.library.get_id()
        self.assertEqual(new_id, 2)

    def test_delete_book(self):
        """Checks the function to delete book by ID."""
        self.library.delete_book(1)
        new_amount_book = len(self.library.books)
        self.assertEqual(new_amount_book, 1)

    def test_update_status(self):
        """Checks the function to update status of book by ID."""
        self.library.update_status(0, 'Выдана')
        status = self.library.books[0]['status']
        self.assertEqual(status, 'Выдана')

    def test_find_by_title(self):
        """Checks the function to find book by title."""
        book = self.library.find_title('first_title')
        book_id = book[0]['id']
        self.assertEqual(book_id, 0)

    def test_find_by_author(self):
        """Checks the function to find book by author."""
        book = self.library.find_author('first_author')
        book_id = book[0]['id']
        self.assertEqual(book_id, 0)

    def test_find_by_year(self):
        """Checks the function to find book by year."""
        book = self.library.find_year(1900)
        book_id = book[0]['id']
        self.assertEqual(book_id, 0)
