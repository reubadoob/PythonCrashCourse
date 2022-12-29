# The code below is used as the basis for the solution. It found on page 97
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

# The solution for this exercise is below
voters = ['jen', 'sarah', 'edward', 'phil', 'alice', 'bob', 'charlie']
for person in voters:
    print("Hello " + person.title() + "!")
    if person in (favorite_languages.keys()):
        print(f"{person.title()}, thank you for taking the poll.")
    else:
        print(f"{person.title()}, please take our poll!")