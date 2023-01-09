joneses = {
    'mjones': {
        'first_name': 'mike',
        'last_name': 'jones',
        'birth_state': 'texas',
        'birth_city': 'houston',
        'age': '37',
        'phone_number': '281-330-8004'
    },
    'njones': {
        'first_name': 'nick',
        'last_name': 'jones',
        'birth_state': 'texas',
        'birth_city': 'dallas',
        'age': '38',
        'phone_number': '281-330-8005'
    },
    'ojones': {
        'first_name': 'orlando',
        'last_name': 'jones',
        'birth_state': 'Texas',
        'birth_city': 'san antonio',
        'age': '39',
        'phone_number': '281-330-8006'
    }
}
for name, personal_info in joneses.items():
    print(f"\nUser Name: {name}")

    full_name = f"{personal_info['first_name']} {personal_info['last_name']}"
    age = f"{personal_info['age']}"
    birth_city = f"{personal_info['birth_city']}"
    phone_numb = f"{personal_info['phone_number']}"

    print(f"\tFull Name: {full_name.title()}")
    print(f"\tAge: {age}")
    print(f"\tBirth City: {birth_city.title()}")
    print(f"\tPhone Number: {phone_numb}")
