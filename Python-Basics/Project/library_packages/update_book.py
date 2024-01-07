
def update_book(book_id, Book_list, file_name):
    for book in Book_list:
        if book['Book ID'] == book_id:
            print(f"Update Book {book_id} Information:")
            book['Book Name'] = input(f"New Book Name ({book['Book Name']}): ")
            book['Genre'] = input(f"New Genre ({book['Genre']}): ")
            book['Language'] = input(f"New Language ({book['Language']}): ")

            new_price = input(f"New Price ({book['Price']}): ")
            try:
                book['Price'] = int(new_price) if new_price else book['Price']
            except ValueError:
                print("Invalid input for price. Keeping the current price.")
            
        with open(file_name, 'w') as f:
                    f.write("Book ID\tBook Name\tGenre\tLanguage\tPrice\n")

                    for b in Book_list:
                        f.write(f"{b['Book ID']}\t{b['Book Name']}\t{b['Genre']}\t{b['Language']}\t{b['Price']}\n")

        print(f"Book {book_id} information updated successfully.")
        return

    print(f"Book with ID {book_id} not found. ")

if __name__ == "__main__":
    pass