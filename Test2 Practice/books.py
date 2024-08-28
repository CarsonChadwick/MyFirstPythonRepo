# Carson Chadwick
# Section 04
# This Program takes excel data about library books and library patrons and organizes it and allows patrons to check out books.
import random
import pandas as pd

class Book():
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.is_all_checked_out = False

    def dispaly_info (self):
        print(self.title + " by " + self.author + " (Genre: " + self.genre + ")")

class Patron():
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name
        self.checked_out_books = []
    
    def check_out_book(self, oBook):
        if oBook.is_all_checked_out == False and len(self.checked_out_books) < 4 :
            self.checked_out_books.append(oBook)
            oBook.is_all_checked_out = True
            print(oBook.title + " has been checked out by " + self.name + ".")
        else:
            print("Cannot check out " + oBook.title + ". Limit reached or book already checked out.")

    def display_checked_out_books(self):
        if len(self.checked_out_books) > 0 :
            print(self.name + " has checked out the following books")
            for book in self.checked_out_books :
                book.dispaly_info()
        else:
            print(self.name + " has no books checked out.")

dfImportedBooks = pd.read_excel("books_data.xlsx")
lstBooks = []
for index, row in dfImportedBooks.iterrows():
    newBook = Book(row['title'], row['author'], row['genre'])
    lstBooks.append(newBook)


dfImportedPatros = pd.read_excel("patrons_data.xlsx")
lstPatrons = []

for index, row in dfImportedPatros.iterrows():
    newPatron = Patron(row['patron_id'], row['name'])
    lstPatrons.append(newPatron)

for patron in lstPatrons :
    numBooks = random.randint(1,4)
    print(patron.name + " will try and check out " + str(numBooks) + " book(s):")
    for num in range(0, numBooks) :
        bookSelect = random.choice(lstBooks)
        patron.check_out_book(bookSelect)
    print()

for patron in lstPatrons :
    patron.display_checked_out_books()
    print()