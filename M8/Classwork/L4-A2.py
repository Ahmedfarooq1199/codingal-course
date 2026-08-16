class Library:
    def __init__(self, list_of_books, name):
        self.books = list_of_books
        self.name = name 
        self.lendDict = {}

def displayBooks(self):
    print(f"We have following books in our library: {self.name}")
    for book in self.booklist:
        print(book)

def lendBook(self, user, book):
    if book not in self.bookslist:
        print("Sorry we do not have that book.")
    elif book in self.lendDict:
        print(f"Book is already being used by {self.lendDict[book]}")
    else:
        self.lendDict[book] = user
        print("Lender-Book database has been updated. You can take the book now.")

    def addBook(self, book):
        if book not in self.bookslist:
            del self.lendDict[book]
            print("Book has been returned. Thank you!")
        else:
            print("That book wasn't borrowed from us.")


if __name__ == '__main__':
    books = Library(['Python',
                     'Rich Dad Poor Dad',
                     'Harry Potter', 'C++ Basics',
                     'Algorithms by CLRS'], "CodeWithHarry")
    
    user_name = input("Welcome to our library. Enter your name: ")
    while True:
        print(f"\nHello {user_name},welcome to the {books.name} library. Enter your choice to continue:")

        print("1. Display all books\n2. Lend a book\n3. Add/Return a book\n4. Exit")
      
        user_choice = input("Enter your choice to continue: ")

        if user_choice not in ['1', '2', '3', '4']:
            print("Please enter you choice to continue: ")
            continue
        if user_choice == '1':
            books.displayBooks()
        elif user_choice == '2':
            book_name = input("Enter the name of the book you want to lend: ")
            books.lendBook(user_name, book_name)
        elif user_choice == '3':
            book_name = input("Enter the name of the book you want to add: ")
            books.addBook(books)
        elif user_choice == '4':
            print("enter the name of the book you want to return")
            books.returnBook(books)
        elif user_choice == '5':
            print(f"Thanks for using the library, {user_name}. Have a great day ahead!")
            break

