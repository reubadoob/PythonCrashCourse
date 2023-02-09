class User:
    def __init__(self, first_name, last_name, age, location, occupation):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.occupation = occupation
        self.login_attempts = 0

    def describe_user(self):
        print(f"User Information: \n\tName: {self.first_name} {self.last_name} \n\tAge: {self.age} \n\tLocation: {self.location} \n\tOccupation: {self.occupation}")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}! Welcome back.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user = User('Mike', 'Jones', 32, 'Houston', 'Lyrical Genius')
user.greet_user()
user.describe_user()

print("Login Attempts:", user.login_attempts)
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

print("Login Attempts:", user.login_attempts)

user.reset_login_attempts()

print("Login Attempts:", user.login_attempts)
