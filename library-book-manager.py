books = []
members = []
id = 100


def add_book():
    new_title = input("Enter the book title: ")
    new_author = input("Enter the author's name: ")
    new_pages = int(input("Enter the number of pages: "))

    new_book = Book(new_title, new_author, new_pages)
    books.append(new_book)

    print("Your book is added!")
    input("Enter to continue! ")


def add_member():
    global id
    member_name = input("Enter your name: ")
    member_age = input("Enter your age: ")
    member_gender = input("what's your gender[Male/Female]: ").lower()
    member_id = id + 1

    new_member = Member(member_name, member_age, member_id, member_gender)

    members.append(new_member)

    print("Member is added")
    input("Enter to continue! ")


def all_books(books):
    for i in range(len(books)):
        print(f"\nBook {i+1}: ")
        books[i].show_books()

def menu():
    print("---------------------------------")
    print("1. Add book")
    print("2. Show all books")
    print("3. Change Book Title")
    print("4. Change Book Author")
    print("5. Change number of pages")
    print("---------------------------------")
    print("6. Add members")
    print("7. Show members")
    print("8. Change member name")
    print("9. Change member age")
    print("10. Change member gender")
    print("---------------------------------")
    print("11. Exit")

def operations(choice, books):
    if choice == 1:
        add_book()
    elif choice == 2:
        if books:
            all_books(books)
            input("Press enter to continue!")
        else:
            print("No books found! ")
            input("Press enter to continue! ")
    elif choice == 3:
        if books:
            all_books(books)
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
            all_books(books)
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
            all_books(books)
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

    elif choice == 11:
        exit = True
        return exit

class Book:
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


    class Member:
        def __init__(self, name, age, member_id, gender ):
            self.name = name
            self.age = age
            self.member_id = member_id
            self.gender = gender

        def show_member(self):
            print(f"Member name: {self.name}")
            print(f"Member age: {self.age}")
            print( f"Member ID: {self.member_id}")
            print(f"gender: {self.gender}")

        def change_name(self, name):
            self.name = name

        def change_age(self, age):
            self.age = age
        
        def change_gender(self, gender):
            self.gender = gender


while True:
    while True:
        try:
            menu()
            choice = int(input("\nEnter the operation number you wanna do: "))
            exit = operations(choice, books)
            if exit:
                break
            else:
                continue

        except:
            print("Only type operation number, try again")
    break
