from dataclasses import dataclass


@dataclass
class Book:
    """Book object representation class."""

    title: str
    author: str
    year: int
    status: str = 'В наличии'

    def add_book_id(self, book_id: int) -> None:
        """Add ID to book object"""
        self.book_id = book_id

    def get_json(self) -> dict:
        """Represent a book object in the json format."""
        data = {
            'book_id': self.book_id,
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'status': self.status
        }
        return data
