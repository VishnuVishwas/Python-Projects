# This fuction will display all the books present in library

def retrieve_book(file_name):
    try:
        with open(file_name, 'r') as f:
            for book in f:
                print(book)
    except FileNotFoundError:
        print(f"The file {file_name} was not found")

if __name__ == "__main__":
        print("The funciton is used display all the books present in library")
