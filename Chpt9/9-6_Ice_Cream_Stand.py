class Restaurant:
    """A class representing a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant name and cuisine type attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Print a description of the restaurant"""
        print(f"This restaurant is called {self.restaurant_name} and they serve {self.cuisine_type} food.")

    def open_restaurant(self):
        """Print a message indicating the restaurant is open"""
        print(f"{self.restaurant_name} is now open!")

# Create a subclass IceCreamStand that inherits from the Restaurant class
class IceCreamStand(Restaurant):
    """A subclass representing an ice cream stand"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes of the parent class and add a list of ice cream flavors"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def display_flavors(self):
        """Print a list of available ice cream flavors"""
        print(f"Available ice cream flavors at {self.restaurant_name}:")
        for flavor in self.flavors:
            print(f"- {flavor}")

# Create an instance of IceCreamStand and add some flavors
ice_cream_stand = IceCreamStand("Scoops", "Ice Cream")
ice_cream_stand.flavors = ["chocolate", "vanilla", "strawberry", "mint chip"]

# Call the display_flavors method to display the available flavors
ice_cream_stand.display_flavors()
