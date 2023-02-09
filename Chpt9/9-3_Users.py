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


user1 = User('John', 'Smith', 42, 'New York', 'software engineer')
user1.describe_user()
user1.greet_user()

user2 = User('Jane', 'Doe', 32, 'Los Angeles', 'graphic designer')
user2.describe_user()
user2.greet_user()

user2 = User('Mike', 'Jones', 32, 'Houston', 'Lyrical Genius')
user2.describe_user()
user2.greet_user()