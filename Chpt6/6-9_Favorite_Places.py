favorite_places = {
    'alice': ['denver', 'colorado springs', 'steamboat springs'],
    'bob': ['memphis', 'nashville', 'knoxville'],
    'charlie': ['portland', 'bend', 'seaside']
}
for name, places in favorite_places.items():
    print(f"\n {name.title()}'s favorite place are:")
    for place in places:
        print(f"\t{place.title()}")
