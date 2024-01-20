import csv
import uuid
from .book import Book
from .user import User

class Library:
    def __init__(self, library_name: str):
        self.library_name = library_name
        self.list_of_books = []
        self.list_of_users = []
        self.file_name = 'books.csv'
        self.load_books_from_csv()

    def add_book(self, book_name: str, book_author: str, genre: str):
        new_book = Book(book_name, book_author, genre)
        self.list_of_books.append(new_book)
        self.save_books_to_csv()

    def remove_book(self, book):
        if book in self.list_of_books:
            self.list_of_books.remove(book)
            print(f"\nBook {book.book_name} was removed from {self.library_name} library")
            self.save_books_to_csv()
        else:
            print(f"\nBook {book.book_name} not found in {self.library_name} library.")

    def save_books_to_csv(self):
        with open(self.file_name, 'w', newline='') as csvfile:
            field_names = ['book_id', 'book_name', 'book_author', 'genre', 'available']
            writer = csv.DictWriter(csvfile, fieldnames=field_names)

            writer.writeheader()
            for book in self.list_of_books:
                writer.writerow({
                    'book_id': book.book_id,
                    'book_name': book.book_name,
                    'book_author': book.book_author,
                    'genre': book.genre,
                    'available': book.available
                })

    def load_books_from_csv(self):
        try:
            with open(self.file_name, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    new_book = Book(row['book_name'], row['book_author'], row['genre'])
                    new_book.book_id = row['book_id']
                    new_book.available = row['available'] == 'True'
                    self.list_of_books.append(new_book)
                print(f"\nBooks loaded from {self.file_name}")
        except FileNotFoundError:
            print(f"\n{self.file_name} not found. No books loaded.")

    def find_book_by_name(self, book_name):
        for book in self.list_of_books:
            if book.book_name.lower() == book_name.lower():
                found_book = book
                break
        return found_book
        
    def add_user(self, user):
        self.list_of_users.append(user)
        print(f"\nUser {user.user_name} was added to {self.library_name} library")

    def remove_user(self, user):
        if user in self.list_of_users:
            self.list_of_users.remove(user)
        else:
            print(f"\n{user.user_name} does not exist.")

    def find_user_by_name(self, user_name):
        for user in self.list_of_users:
            if user.user_name.lower() == user_name.lower():
                found_user = user
                break
        return found_user
        
    def display_all_books(self):
        print(f"\nAll books preset in {self.library_name} library:")
        for book in self.list_of_books:
            book.display_info()
        
    def display_all_users(self):
        print(f"\nAll users in {self.library_name} library:")
        for user in self.list_of_users:
            print(user.user_name)