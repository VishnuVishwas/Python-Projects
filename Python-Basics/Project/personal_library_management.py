# personal_library_management.py

class Book:
    def __init__(self, title, author, genre, publication_date):
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_date = publication_date

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            print(f"{book.title} by {book.author} ({book.genre}, {book.publication_date})")

# Example usage
if __name__ == "__main__":
    my_library = Library()
    my_library.add_book(Book("Jujutsu Kaisen", "Gege Akutami", "Shōnen", "2020"))
    my_library.add_book(Book("Blue Lock", "Muneyuki Kaneshiro ", "Sports", "2022"))
    my_library.display_books()
