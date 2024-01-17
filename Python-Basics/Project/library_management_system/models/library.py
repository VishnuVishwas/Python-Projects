# library.py

import csv
import uuid 
from .book import Book
from .user import User

class Library:
    def __init__(self, library_name: str) -> None:
        self.library_name = library_name
        self.list_of_books = []
        self.list_of_users = []
        self.filename = 'books.csv'

    def add_book(self, book_name: str, book_author: str, genre: str):
        new_book = Book(str(uuid.uuid1()), book_name, book_author, genre)
        self.list_of_books.append(new_book)
        self.save_books_to_csv()

    def remove_book(self, book):
        if book in self.list_of_books:
            self.list_of_books.remove(book)
            print(f"Book {book.book_name} was removed from {self.library_name} library")
        else:
            print(f"Book {book.book_name} not found in {self.library_name} library.")
    
    def save_books_to_csv(self):
        with open(self.filename, 'w', newline='') as csvfile:
            feildnames = ['book_id', 'book_name', 'book_author', 'genre', 'available']
            writer = csv.DictWriter(csvfile, fieldnames=feildnames)

            writer.writeheader()
            for book in self.list_of_books:
                writer.writerow({
                    'book_id' :book.book_id,
                    'book_name': book.book_name,
                    'book_author': book.book_author,
                    'genre': book.genre,
                    'available': book.available,
                })
            
    def load_books_from_csv(self):
        try:
            with open(self.filename, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    new_book = Book(row['book_id'], row['book_name'], row['book_author'], row['genre'])
                    new_book.available = row['available'] == 'True'
                    self.list_of_books.append(new_book)
                print(f"Books loaded from {self.filename}")
        except FileNotFoundError:
            print(f"{self.filename} not found. No books loaded.")
    
    def add_user(self, user):
        self.list_of_users.append(user)
        print(f"User {user.user_name} was added to {self.library_name} library")
        
    def remove_user(self, user):
        if user in self.list_of_users:
            self.list_of_users.remove(user)
            print(f"User {user.user_name} was removed from {self.library_name}")
        else:
            print(f"User {user.user_name} was not found in {self.library_name}")

    def display_all_books(self):
        print(f"All books present in {self.library_name} library: {[book.book_name for book in self.list_of_books]}")

    def display_all_users(self):
        print(f"All users in {self.library_name} library: {[user.user_name for user in self.list_of_users]}")

    def return_book(self, user, book):
        if user in self.list_of_users and book in user.books_borrowed:
            user.return_book(book)
            print(f"Book {book.book_name} returned by {user.user_name}")
        else:
            print(f"Book {book.book_name} could not be returned by {user.user_name}")


if __name__ == "__main__":
    lib = Library("Oxford")

    book1 = Book('1', "jjk", 'anug', 'shonin')
    book2 = Book('2', "Spy X Family", 'vishnu', 'comedy')

    user1 = User('1', 'gojo')

    lib.add_book('Meow wa', 'meowxx', 'Cat verse')
    lib.add_user(user1)

    user1.borrow_book(book1)
    user1.borrow_book(book2)

    lib.display_all_books()
    lib.display_all_users()
    user1.display_borrowed_books()

    # Change this line to call the return_book method on the User object
    user1.return_book(book1)
    user1.display_borrowed_books()