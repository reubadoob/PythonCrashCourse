class User:
    """A class representing a user profile"""

    def __init__(self, first_name, last_name, age, location, occupation):
        """Initialize the first name, last name, age, location, and occupation attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.occupation = occupation

    def describe_user(self):
        """Print a summary of the user's information"""
        print(
            f"\n{self.first_name} {self.last_name} is {self.age} years old, lives in {self.location}, and works as a {self.occupation}.\n")

    def greet_user(self):
        """Print a personalized greeting to the user"""
        print(f"Hello {self.first_name} {self.last_name}! Nice to meet you.")


class Admin(User):
    """A class representing an admin user profile, inheriting from the User class"""

    def __init__(self, first_name, last_name, age, location, occupation):
        """Initialize the first name, last name, age, location, and occupation attributes from the parent class User"""
        super().__init__(first_name, last_name, age, location, occupation)
        self.privileges = Privileges()


class Privileges:
    """A class representing the privileges of an admin user"""

    def __init__(self):
        """Initialize the privileges attribute as an empty list"""
        self.privileges = []

    def show_privileges(self):
        """Print the privileges of the admin user"""
        print("The administrator has the following privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

admin = Admin('Mike', 'Jones', 32, 'Houston', 'Lyrical Genius')
admin.describe_user()
admin.privileges.show_privileges()
print("\nAdding privileges...")
admin_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
admin.privileges.privileges = admin_privileges
admin.privileges.show_privileges()
