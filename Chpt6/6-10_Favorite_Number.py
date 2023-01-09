favorite_num = {
    'alice': ['88', '99', '55'],
    'bob': ['11', '22', '33'],
    'charlie': ['99', '66', '44'],
    'dave': ['18', '36', '54'],
    'evan': ['3', '6', '9']
}
for name, numbers in favorite_num.items():
    print(f"\n{name.title()} favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")
