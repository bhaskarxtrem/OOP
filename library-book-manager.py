books = []

def add_book():
    new_title = input("Enter the book title: ")
    new_author = input("Enter the author's name: ")
    new_pages = int(input("Enter the number of pages: "))

    new_book = book(new_title, new_author, new_pages)
    books.append(new_book)

    print("Your book is added!")
    input("Enter to continue! ")




def menu():
    print("1. Add book")
    print("2. Show all books")
    print("3. Change Book Title")
    print("4. Change Book Author")
    print("5. Change number of pages")
    print("6. Exit")

def operations(choice, books):
    if choice == 1:
        add_book()
    elif choice == 2:
        if books:
            for i in range(len(books)):
                print(f"\nBook {i+1}: ")
                books[i].show_books()
            input("Press enter to continue!")
        else:
            print("No books found! ")
            input("Press enter to continue! ")
    elif choice == 3:
        if books:
            for i in range(len(books)):
                print(f"\nBook {i+1}: ")
                books[i].show_books()
            print("\nHERE IS ALL YOUR BOOKS, CHOOSE THE BOOK NUMBER TO CHANGE BOOK TITLE!")

            while True:
                try:
                    profile = int(input("Enter the book number you wanna change title of: "))
                    new_title = input("Enter the name you wanna upgrade: ")

                    books[profile-1].change_title(new_title)
                    print("Your title is updated!")
                    input("Enter to continue...")
                    break
                except:
                    print("Enter only book number to procced!")
        else:
            print("No books found! ")
            input("Enter to continue! ")
    
    elif choice == 4:
        if books:
            for i in range(len(books)):
                print(f"\nBook {i+1}: ")
                books[i].show_books()
            print("\nHERE IS ALL YOUR BOOKS, CHOOSE THE BOOK NUMBER TO CHANGE BOOK AUTHOR!")

            while True:
                try:
                    profile = int(input("Enter the book number you wanna change author of: "))
                    new_author = input("Enter the name you wanna upgrade: ")

                    books[profile-1].change_author(new_author)
                    print("Your author is updated!")
                    input("Enter to continue...")
                    break
                except:
                    print("Enter only book number to procced!")
        
        else:
            print("No books found! ")
            input("Enter to continue! ")
 
    
    elif choice == 5:
        if books:
            for i in range(len(books)):
                print(f"\nBook {i+1}: ")
                books[i].show_books()
            print("\nHERE IS ALL YOUR BOOKS, CHOOSE THE BOOK NUMBER TO CHANGE BOOK TITLE!")

            while True:
                try:
                    profile = int(input("Enter the book number you wanna change pages of: "))
                    new_pages = int(input("Enter the pages number you wanna update: "))

                    books[profile-1].change_pages(new_pages)
                    print("Your pages is updated!")
                    input("Enter to continue...")
                    break
                except:
                    print("Enter only book number to procced!")
        else:
            print("No books found!")
            input("Enter to continue! ")

    elif choice == 6:
        exit = True
        return exit

class book:
    def __init__(self, title, author, pages):
        self.title = title 
        self.author = author
        self.pages = pages

    def show_books(self):
        print(f"Book name: {self.title}")
        print(f"Book's author: {self.author}")
        print(f"Number of pages in books: {self.pages}")

    def change_title(self, title):
        self.title = title

    def change_author(self, author):
        self.author = author
    
    def change_pages(self, pages):
        self.pages = pages
              

while True:
    while True:
        try:
            menu()
            choice = int(input("Enter the operation number you wanna do: "))
            exit = operations(choice, books)
            if exit:
                break
            else:
                continue

        except:
            print("Only type operation number, try again")
    break
