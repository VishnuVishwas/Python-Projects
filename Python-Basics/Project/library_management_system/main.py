# main.py
from models.book import Book  
from models.user import User
from models.library import Library
if __name__ == "__main__":
    lib = Library("Oxford")

    book1 = Book('1', "jjk", 'anug', 'shonin')
    book2 = Book('2', "Spy X Family", 'vishnu', 'comedy')

    user1 = User('1', 'gojo')

    lib.add_book('Meow wa', 'meowxx', 'Cat verse')
    lib.add_user(user1)

    # Change this line to call the borrow_book method on the User object
    user1.borrow_book(book1)
    user1.borrow_book(book2)

    lib.display_all_books()
    lib.display_all_users()
    user1.display_borrowed_books()

    lib.return_book(user1, book1)
    user1.display_borrowed_books()
