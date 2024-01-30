# contanct management system
import sys

phone_book = {}

def add():
    print("Enter the contact details : ")
    name = input("Enter the name : ")
    number = int(input("Enter the Contact Number : "))

    # phone_book[name] = number
    phone_book.update({name : number})

def remove():
    name = input("Enter the contact name : ")
    if name in phone_book:
        del phone_book[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"Contact '{name}' not found.")

def view() :
    print("Contact details are : ")
    # for name in phone_book:
    # print(name, phone_book[name])
    for x, y in phone_book.items() :
        print(x, y)
    
def phone_management():
    while True:    
        choice = int(input("Choose : \n1. Add Contact\n2. Delete Contact\n3. view contact\n4. Exit\n"))

        if (choice < 0 or choice > 4):
            print("Invalid: Chose from\n1. Add Contact\n2. Delete Contact\n3. view contact\n4. Exit")
            phone_management()
        
        elif choice == 1:
            add()

        elif choice == 2:
            remove()

        elif choice == 3:
            view()

        flag = input("Wanna use phone directory again? if yes 'y' or Quit 'Q' ")
        if(flag.lower() == 'y'):
            phone_management()
        else:
            sys.exit("Have a great day 👋🏻")
        

phone_management()

if __name__ == "__main__":
    pass