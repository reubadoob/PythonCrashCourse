def make_car(manufacturer, model, **optional_features):
    car = {
        'manufacturer': manufacturer,
        'model': model,
    }
    for key, value in optional_features.items():
        car[key] = value
    return car

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)

car = make_car('Mercedes', 'GLX', color='Silver', tow_package=True)
print(car)

car = make_car('BMW', 'M6', color='blue', tow_package=False)
print(car)
