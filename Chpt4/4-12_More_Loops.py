foods = [my_foods for my_foods in ['pita', 'flafel', 'gyro']]
friends_foods = foods[:]
print(foods)
print(friends_foods)
for food in foods:
    print(food.upper())
for friends_food in friends_foods:
    print(friends_food.title())