# user.py

from .book import Book

class User:
    def __init__(self, user_name) -> None:
        self.user_name = user_name
        self.books_borrowed = []

    # borrow book
    def borrow_book(self, book):
        if book not in self.books_borrowed:
            self.books_borrowed.append(book)  # Fixed typo here
            book.available = False
            print(f"\n{self.user_name} borrowed {book.book_name}.")
        else:
            print(f"\n{book.book_name} is not available.")
    
    # return book
    def return_book(self, book):
        if book in self.books_borrowed:
            self.books_borrowed.remove(book)
            book.available = True
            print(f"\n{self.user_name} returned {book.book_name}.")
        else:
            print(f"\n{self.user_name} did not borrow {book.book_name}.")

    # display books borrowed
    def display_borrowed_books(self):
        print(f"\n{self.user_name}'s borrowed books: ")
        for book in self.books_borrowed:
            book.display_info()