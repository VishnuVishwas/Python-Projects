# book api 
import json

# get method
import json

def get_all_books():
    try:
        with open('books.json', 'r') as file:
            books = json.load(file)
            return books
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# get method  
def get_book_by_id(book_id):
    with open('books.json', 'r') as file:
        books = json.load(file)
        for book in books:
            if book['id'] == book_id:
                return book

# Post method 
def create_new_book(new_book):
    with open('books.json', 'r') as file:
        books = json.load(file)
    
    books.append(new_book)
    
    with open('books.json', 'w') as file:
        json.dump(books, file, indent=2)

# put method
def update_book(book_id, updated_data):
    with open('books.json', 'r+') as file:
        books = json.load(file)
        for book in books:
            if book['id'] == book_id:
                book.update(updated_data)
                break 

    with open('books.json', 'w') as file:
        json.dump(books, file, indent=2)

# delete method
def delete_book(book_id):
    with open('books.json', 'r+') as file:
        books = json.load(file)
        books = [book for book in books if book['id'] != book_id]

    with open('books.json', 'w') as file:
        json.dump(books, file, indent=2)

if __name__ == '__main__':
    all_books = get_all_books()
    print("All books:")
    for book in all_books:
        print(f"\nBook {book['title']}\nAuthor {book['author']}\n")

    print("Book by id: ")
    specific_book = get_book_by_id(2)
    print(f"\nBook {specific_book['title']}\nAuthor {specific_book['author']}\n")

    new_book = {"id": 4, "title": "The Alchemist", "author": "Paulo Coelho"}
    create_new_book(new_book)

    updated_book_data = {"title": "The Catcher in the Rye", "author": "J.D. Salinger (Updated)"}
    update_book(4, updated_book_data)

    delete_book(1)
    print('\nBook Deleted: Book ID 1')
