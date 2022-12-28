rivers = {
    'Mississippi': 'North America',
    'Nile': 'Egypt',
    'Amazon': 'Brazil'
}

for river, country in rivers.items():
    print(f"\nThe {river} river flows through {country}")

for river in rivers.keys():
    print(f"\n{river}")

for country in rivers.values():
    print(f"\n{country}")