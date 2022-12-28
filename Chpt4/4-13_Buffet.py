buffet_meats = ('Ham', 'Prime Rib')
buffet_vegg = ('Mashed potatoes', 'Broccoli')
buffet_dessert = ('Apple Pie', )
for buffet_meat in buffet_meats:
    print(f" The meat options are {buffet_meat}")
for buffet_veg in buffet_vegg:
    print(f" The veggie options are {buffet_veg}")
for buffet_dessert in buffet_dessert:
    print(f" The dessert option is {buffet_dessert}")
buffet_dessert = ('Chocolate Cake', 'Cheese Cake')
for buffet_dessert in buffet_dessert:
    print(f"The new dessert menu is {buffet_dessert}")
buffet_dessert.append('Chocolate Cake')

