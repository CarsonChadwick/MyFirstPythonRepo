def menu() :
    iInput = 0
    while (iInput != 4) :
        print("1. Add")
        print("2. Delete")
        print("3. Search")
        print("4. Exit")
        iInput = int( input("Choose a menu item (1, 2, 3, 4): "))
        
        if (iInput == 1) :
            add()
        elif (iInput == 2) :
            delete()
        elif (iInput == 3) :
            search()


#function that someday will add a student
def add() :
    print("\nAdd a student\n")

#function that someday will delete a student
def delete() :
    print("\nDelete a student\n")

#function that someday will search for a student
def search() :
    print("\nSearch for a student\n")

def exit() :
    print("\nThank you. Please come again!\n")

#Our Main Program begins here
print("Welcome to our program")
menu()

exit()