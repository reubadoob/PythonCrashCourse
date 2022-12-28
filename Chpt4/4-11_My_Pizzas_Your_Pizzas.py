toppings = ['pineapple', 'jalpenos', 'sausage']
for topping in toppings:
    print(f"I like the following {topping} on my pizza")

print("I really love pizza")
favorite_pizza = ['Hawaiian', 'BBQ Chicken', 'Thai Chicken']
friend_favorite = favorite_pizza[:]
print(f"My favorite pizzas are {favorite_pizza[:]}")
print(f"My friends favorite pizzas are {friend_favorite[:]}")
favorite_pizza.append('Margehrita')
friend_favorite.append('Cheese')
print(f"My favorite pizzas are {favorite_pizza[:]}")
print(f"My friends favorite pizzas are {friend_favorite[:]}")
