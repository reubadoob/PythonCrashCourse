states = ['Kansas', 'Maryland', 'Colorado', 'Utah', 'Tennessee', 'Oregon', 'North Carolina', 'Washington', 'Nevada']
print(states)
print(len(states))
states.append('Florida')
print(states)
del states[0]
print(states)
states[0] = 'Kansas'
print(states)
current = states.pop(-1)
print(f"I currently live in {current}")
states.remove('Kansas')
print(states)
print(sorted(states))
print(states)
states.sort()
print(states)
states.reverse()
print(states)
print(len(states))
