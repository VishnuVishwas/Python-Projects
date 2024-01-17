# user.py
from .book import Book 

class User:
    def __init__(self, user_id: str, user_name: str) :
        self.user_id = user_id
        self.user_name = user_name
        self.books_borrowed = []

    def borrow_book(self, book):
        if book.check_availability():
            self.books_borrowed.append(book)
            book.available = False
            print(f"Book: {self.user_name} borrowed {book.book_name}")
        else:
            print(f"Sorry {book.book_name} is not available.")

    def return_book(self, book):
        if book in self.books_borrowed:
            self.books_borrowed.remove(book)
            book.available = True
            print(f"{self.user_name} returned {book.book_name}")
        else:
            print(f"{self.user_name} did not borrow {book.book_name}")
            
    def display_borrowed_books(self):
            print(f"{self.user_name}'s borrowed books: {[book.book_name for book in self.books_borrowed]}")
        
if __name__ == "__main__":
    # book = Book('1', "jjk", 'anug', 'shonin')
    pass
    # book.display_info()

    # user = User('1', 'gojo')
    # user.borrow_book(book)

    # user.return_book(book)
    