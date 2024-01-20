# book.py 

import uuid

class Book:
    def __init__(self, book_name: str, book_author: str, genre: str) -> None:
        self.book_id = str(uuid.uuid1())
        self.book_name = book_name
        self.book_author = book_author
        self.genre = genre
        self.available = True

    def check_availability(self):
        return self.available

    def display_info(self):
        print(f"\nBook ID: {self.book_id}\nTitle: {self.book_name}\nAuthor: {self.book_author}\nGenre: {self.genre}")