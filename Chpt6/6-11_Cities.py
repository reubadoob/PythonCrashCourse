cities = {
    'Memphis': {
        'county': 'shelby',
        'population': '620702',
        'fact': 'Bluff City'
    },
    'Portland': {
        'county': 'multnomah',
        'population': '714360',
        'fact': 'City of Roses',
    },
    'Denver':  {
        'county': 'denver county',
        'population': '2931000',
        'fact': 'Mile High City'
    },
}
for city, city_info in cities.items():
    print(f"\nCity Name: {city}")

    county = f"{city_info['county']}"
    population = f"{city_info['population']}"
    fact = f"{city_info['fact']}"

    print(f"\tCounty: {county.title()}")
    print(f"\tPopulation: {population}")
    print(f"\tFact: {fact}")
