import random

lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
winning_numbers = random.sample(lottery_pool, 4)

print(f"Any ticket matching these 4 numbers or letters wins a prize: {winning_numbers}")
