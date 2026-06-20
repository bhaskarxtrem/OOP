users = []
current_user = None
new_user = None

def menu():
    print("1. Create user")
    print("2. Show all users")
    print("3. Change user age")
    print("4. Change user name")

def create_user():
    user_name = input("Enter your name: ")
    user_age = input("Enter your age: ")


class user:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_profile(self):
        print(f"name: {self.name}")
        print(f"Age: {self.age}")



    