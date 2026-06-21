users = []

def menu():
    print("1. Create user")
    print("2. Show all users")
    print("3. Change user name")
    print("4. Change user age")
    print("5. Exit")


def operations(choice, users):
    if choice == 1:
        create_user()

    elif choice == 2:
        for i in range(len(users)):
            print(f"\nPROFILE {i+1}:")
            users[i].show_profile()
        input("Press enter to continue...")
        

    elif choice == 3:
        for i in range(len(users)):
            print(f"PROFILE {i+1}:")
            users[i].show_profile()
        print("\nHERE ARE ALL THE PROFILE, SELECT PROFILE NUMBER TO UPDATE NAME!")

        while True:
            try:
                profile = int(input("\nWhat profile number you wanna change: "))
                new_name = input("Enter the name you want to update: ")
        
                users[profile-1].change_name(new_name)
                print("Your name is updated!")
                input("Enter to continue...")
                break
            except:
                print("Only type profile number to procced")

    elif choice == 4:
        for i in range(len(users)):
            print(f"PROFILE {i+1}:")
            users[i].show_profile()
        print("\nHERE ARE ALL THE PROFILE, SELECT PROFILE NUMBER TO UPDATE AGE OF...")

        while True:
            try:
                profile = int(input("\nWhat profile Number you wanna change: "))
                new_age = input("Enter the age you want to update: ")
        
                users[profile-1].change_age(new_age)
                print("Your age is updated!")
                input("Enter to continue...")
                break
            except:
                print("Only type profile number to procced")

    elif choice == 5:
        exit = True
        return exit



def create_user():
    name_input = input("Enter your name: ")
    age_input = input("Enter your age: ")

    new_user = user(name_input, age_input)
    users.append(new_user)

    print("Your account is created! ")

    


class user:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_profile(self):
        print(f"Name is {self.name}, and age is {self.age}")

    def change_name(self, name):
        self.name = name

    def change_age(self, age):
        self.age = age




while True:
    while True:
        try:
            menu()
            choice = int(input("What operation you wanna do: "))
            exit = operations(choice, users)
            if exit:
                break
            else:
                continue
        except:
            print("Only type operation number to procced...")

    break






    