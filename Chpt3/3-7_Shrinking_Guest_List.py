guestlist = ["Michael Jordan", "Jordan Peterson", "Voddie Baucham"]
print(f"{guestlist[0]}, You are invited to a BBQ!")
print(f"{guestlist[1]}, You are invited to a BBQ!")
print(f"{guestlist[2]}, You are invited to a BBQ!")
print(f"{guestlist[2]}, is unable to attend the BBQ")
del guestlist [2]
guestlist.append( 'Alex Jones')
print(f"{guestlist[0]}, You are invited to a BBQ!")
print(f"{guestlist[1]}, You are invited to a BBQ!")
print(f"{guestlist[2]}, You are invited to a BBQ!")
print("I've found a bigger table!")
guestlist.insert(0, 'Martha Stewart')
guestlist.insert(3, 'Snoop Dogg')
guestlist.append('Ron Paul')
print(f"{guestlist[0]}, You are invited to a BBQ!")
print(f"{guestlist[3]}, You are invited to a BBQ!")
print(f"{guestlist[-1]}, You are invited to a BBQ!")
print("Mom says I can' only invite 2 people since the basement is small")
removal1 = guestlist.pop(0)
print(f"Sorry {removal1} you can't come because mom said so")
removal2 = guestlist.pop(0)
print(f"Sorry {removal2} you can't come because mom said so")
removal3 = guestlist.pop(0)
print(f"Sorry {removal3} you can't come because mom said so")
removal4 = guestlist.pop(1)
print(f"Sorry {removal4} you can't come because mom said so")
print(f"{guestlist[0]} you are still invited!")
print(f"{guestlist[1]} you are still invited!")
del guestlist[0]
del guestlist[1]
print(guestlist)