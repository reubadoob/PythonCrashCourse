requested_toppings = ['ketchup', 'mustard', 'pickles', 'lettuce']
print("Is ketchup a requested topping?")
print('ketchup' in requested_toppings)

print("Are jalapenos a requested topping?")
print('jalapenos' in requested_toppings)

one = 1
print("\nIs 1 == 1? I predict True")
print(one == 1)

age_0 = 19
age_1 = 21
print("\nIs age_0 > age_1)?")
print(age_0 > age_1)
print("Is age_0 < age_1)?")
print(age_0 < age_1)
print("Is age_0 = age_1?")
print(age_0 == age_1)
print("Is age_0 >= 21 and age_1 >=0 ?")
print(age_0 >= 21 and age_1 >=0)
print("age_0 >= 21 or age_1 >= 21")
print(age_0 >= 21 or age_1 >= 21)

motorcycles = ['ducati', 'yamaha', 'kawasaki', 'suzuki', 'honda']
bike = 'suzuki'
if bike in motorcycles:
    print(f"\n{bike.title()} is a Crotch Rocket ")
bike = 'harley-davidson'
if bike not in motorcycles:
    print(f"\n{bike.title()} is not a Crotch Rocket")
