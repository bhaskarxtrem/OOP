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
    while True:
        member_gender = input("what's your gender[Male/Female]: ").lower()
        if member_gender == "male" or member_gender == "female":
            member_gender = member_gender.capitalize()
            break
        else:
            print("Invalid Gender! try again.")
    
    id += 1

    member_id = id

    new_member = Member(member_name, member_age, member_id, member_gender)

    members.append(new_member)

    print("Member is added")
    input("Enter to continue! ")


def remove():
    if books:
        all_books(books)
        print("\nHERE ARE ALL THE BOOKS, SELECT THE BOOK NUMBER TO REMOVE IT! ")
        while True:
            try:
                book = int(input("Enter the book number you wanna remove: "))
                books.pop(book - 1)

                print("Your book is removed! ")
                input("Enter to continue! ")
                break


            

            except:
                print("Only type book number to procced! ")
                input("Enter to continue! ")

    else:
        print("No books found! ")
        input("Enter to continue! ")
                

def all_books(books):
    for i in range(len(books)):
        print(f"\nBook {i+1}: ")
        books[i].show_books()

def all_members(members):
    for i in range(len(members)):
        print(f"\nMember {i+1}: ")
        members[i].show_member()

def menu():
    print("---------------------------------")
    print("1. Add book")
    print("2. Show all books")
    print("3. Change Book Title")
    print("4. Change Book Author")
    print("5. Change number of pages")
    print("6. Remove book")
    print("---------------------------------")
    print("7. Add members")
    print("8. Show members")
    print("9. Change member name")
    print("10. Change member age")
    print("11. Change member gender")
    print("---------------------------------")
    print("12. Exit")

def operations(choice, books, members):
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

                    books[profile - 1].change_title(new_title)
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

                    books[profile - 1].change_author(new_author)
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

                    books[profile - 1].change_pages(new_pages)
                    print("Your pages is updated!")
                    input("Enter to continue...")
                    break
                except:
                    print("Enter only book number to procced!")
        else:
            print("No books found! ")
            input("Enter to continue! ")

    elif choice == 6:
        remove()

    elif choice == 7:
        add_member()

    elif choice == 8:
        if members:
            all_members(members)
            input("Enter to continue! ")
        else:
            print("No members found! ")
            input("Enter to continue! ")

    elif choice == 9:
        if members:
            all_members(members)
            print(f"\nTHESE ARE ALL THE MEMBERS OF LIBRARY, CHOOSE THE MEMBER NUMBER TO UPDATE NAME! ")

            while True:
                try:
                    member = int(input("Enter the member number to change name: "))
                    new_name = input("Enter the name you wanna update: ")
                    members[member - 1].change_name(new_name)
                    print("Your name is updated! ")
                    input("Enter to continue! ")
                    break
                except:
                    print("Enter only member number to procced! ")

        else:
            print("No members found! ")
            input("Enter to continue! ")

    elif choice == 10:
        if members:
            all_members(members)
            print(f"\nTHESE ARE ALL THE MEMBERS OF LIBRARY, CHOOSE THE MEMBER NUMBER TO UPDATE AGE! ")

            while True:
                try:
                    member = int(input("Enter the member number to change age: "))
                    new_age = input("Enter the age you wanna update: ")
                    members[member - 1].change_age(new_age)
                    print("Your age is updated! ")
                    input("Enter to continue! ")
                    break
                except:
                    print("Enter only member number to procced! ")

        else:
            print("No members found! ")
            input("Enter to continue! ")

    elif choice == 11:
        if members:
            all_members(members)
            print(f"\nTHESE ARE ALL THE MEMBERS OF LIBRARY, CHOOSE THE MEMBER NUMBER TO UPDATE GENDER! ")

            while True:
                try:
                    member = int(input("Enter the member number to change Gender: "))
                    while True:
                        new_gender = input("What Gender you wanna update [Male/Female]: ").lower()
                        if new_gender == "male" or new_gender == "female":
                            new_gender = new_gender.capitalize()
                            break
                        else:
                            print("Invalid Gender! try again.")
                    members[member - 1].change_gender(new_gender)
                    print("Your Gender is updated! ")
                    input("Enter to continue! ")
                    break
                except:
                    print("Enter only member number to procced! ")

        else:
            print("No members found! ")
            input("Enter to continue! ")


    elif choice == 12:
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
        print(f"Gender: {self.gender}")

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
            exit = operations(choice, books, members)
            if exit:
                break
            else:
                continue

        except:
            print("Only type operation number, try again")
    break
