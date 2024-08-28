from datetime import datetime
class Item():
    def __init__(self, title):
        self.title = title
        self.dateCreated = datetime.now()
    def description(self):
        print("This item was created on", self.dateCreated.date(), "at",
 self.dateCreated.ctime())
        
class Books(Item) :
    def __init__(self, title, author, year, genre):
        super().__init__(title)
        self.author = author
        self.year = year
        self.genre = genre
    
    def printShoe(self):
        self.description()
        print(self.title + " by " + self.author)
        
        

bookList = []
bookNumber = int(input("How many books would you like to add? "))
for icount in range(0, bookNumber) :
    title = input("What is the book " + str(icount + 1) + "'s title? ")
    author = input("Who is the author? ")
    year = input("What year was it published? ")
    genre = input("What is the genre? ")
    print("")
    bookList.append(Books(title, author, year, genre))

for books in bookList :
    books.printShoe()
