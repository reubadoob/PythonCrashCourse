class User:
    def __init__(self, first_name, last_name, age, location, occupation):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.occupation = occupation

    def describe_user(self):
        print(
            f"\n{self.first_name} {self.last_name} is {self.age} years old, lives in {self.location}, and works as a {self.occupation}.\n")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}! Nice to meet you.")

class Admin(User):
    def __init__(self, first_name, last_name, age, location, occupation):
        super().__init__(first_name, last_name, age, location, occupation)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print(f"{self.first_name} {self.last_name} has the following privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

# Create an instance of Admin
admin = Admin("John", "Doe", 30, "New York", "Software Engineer")

# Call the show_privileges method
admin.show_privileges()
