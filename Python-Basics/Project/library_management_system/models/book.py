class Book:
    def __init__(self, book_id: str, book_name: str, book_author: str, genre: str):
        self.book_id = book_id
        self.book_name = book_name
        self.book_author = book_author
        self.genre = genre
        self.available = True

    def display_info(self):
        print(f"Title: {self.book_name}\nAuthor: {self.book_author}\nGenre: {self.genre}")

    def check_availability(self):
        return self.available
