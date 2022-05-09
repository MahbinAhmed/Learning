# # Project-3 (Library Management System)
class library:
    def __init__(self,listofBook):
        self.books=listofBook
    
    def displayBooks(self):
        print("Available books are: \n")
        for book in self.books:
            print(" #", book)
        
    def borrowBookS(self,bookName):
        if bookName in self.books:
            print("You have succesfully borrowed {bookName} from us . Keep it safely and return within 30 days ")
            self.books.remove(bookName)
            return True
        else :
            print("Sorry, This book is currently not available")
            return False
    def returnBooks(self,bookName):
        self.books.append(bookName)
        print("Thanks for returning the book. Hope you have enjoyed the book. Thank you!")

class student:
    def requestBook(self):
        self.books = input("Enter the name of the book that you want to borrow: ")
        return self.books

    def returningBook(self):
        self.books = input("Enter the name of the book that you want to return: ")
        return self.books

lowner = library(["Student Hacks","Graphics Design","Thakumar Jhuli","Python Basic","Life Hacks"])
s1 = student()

while(True):
    wlmsg='''=====Welcome to the library=====\n
    1. Show the list of the books
    2. Borrow a book
    3. Return a book
    4. Exit the library'''
    print(wlmsg)
    a = int(input("Enter you choose: "))
    if a == 1:
        lowner.displayBooks()
    elif a == 2:
        lowner.borrowBookS(s1.requestBook())
    elif a == 3:
        lowner.returnBooks(s1.returningBook())
    elif a == 4:
        print("Thanks for using our library")
        exit()
    else:
        print("Invalid Input")