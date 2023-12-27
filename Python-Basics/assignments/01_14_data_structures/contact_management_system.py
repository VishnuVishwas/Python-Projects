# contanct management system
import sys

phoneBook = {}

def add():
    print("Enter the contact details : ")
    name = input("Enter the name : ")
    number = int(input("Enter the Contact Number : "))

    # phoneBook[name] = number
    phoneBook.update({name : number})

def remove():
    name = input("Enter the contact name : ")
    if name in phoneBook:
        del phoneBook[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"Contact '{name}' not found.")

def view() :
    print("Contact details are : ")
    # for name in phoneBook:
    # print(name, phoneBook[name])
    for x, y in phoneBook.items() :
        print(x, y)
    
def phoneManagement():
    while True:    
        choice = int(input("Choose : \n1. Add Contact\n2. Delete Contact\n3. view contact\n4. Exit\n"))

        if (choice < 0 or choice > 4):
            print("Invalid: Chose from\n1. Add Contact\n2. Delete Contact\n3. view contact\n4. Exit")
            phoneManagement()
        
        elif choice == 1:
            add()

        elif choice == 2:
            remove()

        elif choice == 3:
            view()

        flag = input("Wanna use phone directory again? if yes 'y' or Quit 'Q' ")
        if(flag.lower() == 'y'):
            phoneManagement()
        else:
            sys.exit("Have a great day 👋🏻")
        

phoneManagement()