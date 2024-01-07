# Function is used to delete a book based on ID
def delete_book(book_id, file_name, Book_list):
    for book in Book_list:
        if book['Book ID'] == book_id:
            Book_list.remove(book)
            update_file(file_name, Book_list)  # Update the file
            print(f"Book with ID {book_id} deleted successfully.")
            return
    
    print(f"Book with ID {book_id} not found.")

def update_file(file_name, Book_list):
    with open(file_name, 'w') as f:
        f.write(f"Book ID\tBook Name\tGenre\tLanguage\tPrice\n")

        for book in Book_list:
            f.write(f"{book['Book ID']}\t{book['Book Name']}\t{book['Genre']}\t{book['Language']}\t{book['Price']}\n")

if __name__ == "__main__":
        print("The funciton is used to delete a book")
