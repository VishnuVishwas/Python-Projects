# main.py
from models.library import Library
from models.user import User

def main():
    libraries = []

    while True:
        print("\nMenu:")
        print("1. Create a new library")
        print("2. Select a library")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            library_name = input("Enter the name of the new library: ")
            new_library = Library(library_name)
            libraries.append(new_library)
            print(f"\nLibrary '{library_name}' created.")

        elif choice == "2":
            if not libraries:
                print("\nNo libraries available. Please create a new library.")
                continue

            print("\nAvailable Libraries:")
            for i, library in enumerate(libraries, 1):
                print(f"{i}. {library.library_name}")

            library_index = input("Enter the library number: ")
            try:
                library_index = int(library_index) - 1
                selected_library = libraries[library_index]
                manage_library(selected_library)
            except (ValueError, IndexError):
                print("\nInvalid library selection. Please try again.")

        elif choice == "3":
            break

        else:
            print("\nInvalid choice. Please try again.")


def manage_library(library):
    while True:
        print("\nLibrary Menu:")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Display all books")
        print("4. Add a user")
        print("5. Remove a user")
        print("6. Display all users")
        print("7. Borrow a book")
        print("8. Return a book")
        print("9. Back to main menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            book_name = input("Enter the book name: ")
            book_author = input("Enter the book author: ")
            genre = input("Enter the book genre: ")
            library.add_book(book_name, book_author, genre)

        elif choice == "2":
            book_name = input("Enter the book name you want to remove: ")
            book = library.find_book_by_name(book_name)
            if book:
                library.remove_book(book)
            else:
                print(f"Book {book_name} not found in the library.")

        elif choice == "3":
            library.display_all_books()

        elif choice == "4":
            user_name = input("Enter the user name: ")
            user = User(user_name)
            library.add_user(user)

        elif choice == "5":
            user_name = input("Enter the user name you want to remove: ")
            user = library.find_user_by_name(user_name)
            if user:
                library.remove_user(user)
            else:
                print(f"User {user_name} not found in the library.")

        elif choice == "6":
            library.display_all_users()

        elif choice == "7":
            user_name = input("Enter your name: ")
            user = library.find_user_by_name(user_name)
            if user:
                book_name = input("Enter the book name you want to borrow: ")
                book = library.find_book_by_name(book_name)
                if book:
                    user.borrow_book(book)
                    break  # Break the loop after successful book borrowing
                else:
                    print(f"Book {book_name} not found in the library.")
            else:
                print(f"User {user_name} not found in the library.")

        elif choice == "8":
            user_name = input("Enter your name: ")
            user = library.find_user_by_name(user_name)
            if user:
                user.display_borrowed_books()
                book_name = input("Enter the book name you want to return: ")
                
                # Find the book by name in the user's borrowed books
                book = library.find_book_by_name(book_name)
                
                if book:
                    user.return_book(book)
                else:
                    print(f"Book {book_name} not found in your borrowed books.")
            else:
                print(f"User {user_name} not found in the library.")

        elif choice == "9":
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
