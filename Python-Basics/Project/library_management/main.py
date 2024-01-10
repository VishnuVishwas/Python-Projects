# main.py

from models.library import Library

state_centre_library = Library('State Centre')

def add_books():
    state_centre_library.add_book('You can', 500)  
    state_centre_library.add_book('The power of subconscious', 350)
    state_centre_library.add_book('Atomic Habits', 550)

def view_all_books():
    print("Books in library are: ")
    state_centre_library.show_books()

def delete_book():
    view_all_books()
    book_id = input("Enter the ID of the book you want to delete: ")
    state_centre_library.delete_book(book_id)

def view_book():
    view_all_books()
    book_id = input("Enter the ID of the book you want to view: ")
    state_centre_library.retrive_book(book_id)

if __name__ == "__main__":
    add_books()
    view_all_books()
    delete_book()
    view_book()

