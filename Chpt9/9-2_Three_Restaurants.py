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

restaurant1 = Restaurant("McDonald's", "Fast Food")
restaurant2 = Restaurant("Applebees", "American")
restaurant3 = Restaurant("Olive Garden", "Italian")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()