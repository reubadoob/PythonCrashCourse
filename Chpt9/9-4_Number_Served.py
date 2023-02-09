class Restaurant:
    """A class representing a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant name and cuisine type attributes"""
        self.number_served = 0
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Print a description of the restaurant"""
        print(f"This restaurant is called {self.restaurant_name} and they serve {self.cuisine_type} food.")

    def open_restaurant(self):
        """Print a message indicating the restaurant is open"""
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, number_served):
        """Allow user to set the number of customers that have been served."""
        self.number_served = number_served

    def increment_number_served(self, number_served):
        """Allow user to increment the number of customers served."""
        self.number_served += number_served

restaurant = Restaurant("Taco Bell", "Mexican")

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
print("\nNumber served: " + str(restaurant.number_served))

restaurant.set_number_served(777)
print("Number served: " + str(restaurant.number_served))

restaurant.increment_number_served(666)
print("Number served: " + str(restaurant.number_served))

