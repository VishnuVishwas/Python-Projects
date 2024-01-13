# Child class - Library
from models.book import Book

class Library():
    def __init__(self, library_name: str) :
        self.library_name = library_name
        self.books = []
    
    # add book to library
    def add_book(self, book_name: str, book_price: int):
        book_id = str(len(self.books) + 1)
        book = Book(book_id, book_name, book_price)
        self.books.append(book)
        print(f"Book '{book.book_name}' added into library '{self.library_name}'")

    # show deatails of all books
    def show_books(self):
        for book in self.books:
                book.show_details()

    # show details of book using ID
    def retrive_book(self, book_id: str):
        for book in self.books:
            if book.book_id == book_id:
                print(f"Retrieving book details for ID {book_id} ")
                book.show_details()
                return
        print(f"Book with ID {book_id} was not found.")
    
    # update book based on ID
    def update_book(self, book_id: str, new_name: str, new_price: int):
        for book in self.books:
            if book.book_id == book_id:
                book.book_name = new_name
                book.book_price = new_price
                print(f"The book with ID {book_id} was updated.")
                book.show_details()
                break
        else:
            print(f"The book with ID {book_id} not found.")

    # delete book 
    def delete_book(self, book_id: str):
        for index, book in enumerate(self.books):
            if book.book_id == book_id:
                deleted_book = self.books.pop(index)
                print(f"Book '{book_id}' with name '{book.book_id}' was deleted.")
                break
        else:
            print(f"No book found with ID {book_id}")