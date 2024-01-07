from library_packages import create_book
from library_packages import update_book
from library_packages import retrieve_book
from library_packages import delete_book
import sys

class Library:
    def __init__(self):
        self.user_input = 0 

    def PersonalLibraryManagement(self, file_name, Book_list):
        self.user_input = int(input("Enter your choice : \n1. Create\n2. Update\n3. Retrieve\n4. Delete\n"))

        if self.user_input < 1 or self.user_input > 4:
            print("Invalid Input")
            return

        if self.user_input == 1:
            print("Creating a file\n")
            create_book.create_book(file_name, Book_list)

        elif self.user_input == 2:
            book_id = int(input("Enter book_id\n"))
            update_book.update_book(book_id, Book_list, file_name)

        elif self.user_input == 3:
            retrieve_book.retrieve_book(file_name)

        elif self.user_input == 4:
            book_id = int(input("Enter book_id\n"))
            delete_book.delete_book(book_id, file_name, Book_list)

if __name__ == "__main__":
    file_name = input("Enter the file name to be created : ")
    Book_list = []

    try:
        with open(file_name, 'w') as f:
            f.write("Personal Library Management System\n")
        print("File " + file_name + " created successfully. ")
    except IOError:
        print("Error: could not create file " + file_name)

    lib_instance = Library()

    while True:
        lib_instance.PersonalLibraryManagement(file_name, Book_list)

        play_again = input("Want to continue : Yes 'y' or Quit 'Q' ")
        if play_again.lower() != 'y':
            sys.exit()
