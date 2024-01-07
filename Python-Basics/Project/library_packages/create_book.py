# Functon to create a book 

def create_book(file_name, Book_list):
    print("Enter the book details. ")
    book_id = int(input("Enter Book id : "))
    book_name = input("Book name : ")
    genre = input("Genre : ")
    language = input("Language : ")    
    price = int(input("Price : "))

    book_info = {
        "Book ID": book_id,
        "Book Name": book_name,
        "Genre": genre,
        "Language": language,
        "Price": price 
    }

    Book_list.append(book_info)
    with open(file_name, 'w') as f:
        print(f"Book ID\tBook Name\tGenre\tLanguage\tPrice\n")

        for book in Book_list:
            f.write(f"{book['Book ID']}\t{book['Book Name']}\t{book['Genre']}\t{book['Language']}\t{book['Price']}\n")
    print("Book info added successfully.")

if __name__ == "__main__":
    print("The funciton is used to create a book")

