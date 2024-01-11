# book.py

class Book:
    def __init__(self, book_id: str, book_name: str, book_price: int):
        self.book_id = book_id
        self.book_name = book_name
        self.book_price = book_price
    
    # show book details
    def show_details(self):
        print("-------------------------------")
        print("Book Details:")
        print("ID:", self.book_id)
        print("Name:", self.book_name)
        print("Price:", self.book_price)
        print("-------------------------------")
