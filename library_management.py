class Library:

    def __init__(self):
        self.books = {}

    def add_book(self):
        book = input("Enter Book Name: ")
        author = input("Enter Author Name: ")
        copies = int(input("Enter Number of Copies: "))

        self.books[book] = {"Author": author, "Copies": copies}

        print("Book Added Successfully.")

    def display_books(self):

        if len(self.books) == 0:
            print("No Books Available.")
        else:
            print("\nLibrary Books")
            print("-" * 40)

            for book in self.books:
                print("Book   :", book)
                print("Author :", self.books[book]["Author"])
                print("Copies :", self.books[book]["Copies"])
                print("-" * 40)

    def borrow_book(self):

        book = input("Enter Book Name to Borrow: ")

        if book in self.books:

            if self.books[book]["Copies"] > 0:
                self.books[book]["Copies"] -= 1
                print("Book Borrowed Successfully.")
            else:
                print("Book is Not Available.")

        else:
            print("Book Not Found.")

    def return_book(self):

        book = input("Enter Book Name to Return: ")

        if book in self.books:
            self.books[book]["Copies"] += 1
            print("Book Returned Successfully.")
        else:
            print("Book Not Found.")


lib = Library()

while True:

    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        lib.add_book()

    elif choice == 2:
        lib.display_books()

    elif choice == 3:
        lib.borrow_book()

    elif choice == 4:
        lib.return_book()

    elif choice == 5:
        print("Thank You!")
        break

    else:
        print("Invalid Choice.")
