guests = ['Adriana', 'Irina', 'Matika', 'Lana']
print(guests)
cant_come = guests.pop(-2)
guests.append('Lisa')
print(f"{guests} is coming, {cant_come} couldnt come tho")



for guest in guests:
    print(f"{guest}, I found a bigger table!")

guests.insert(0, "mia".title())
guests.insert(3, "mona".title())
guests.append("mia".title())
guests.sort(reverse=True)
print(guests)
print(sorted(guests))
print("Im sorry guys, there is only place for two people")

pop_guest = guests.pop()
print(f"Im sorry, you cant come {pop_guest}")
pop_guest = guests.pop()
print(f"Im sorry, you cant come {pop_guest}")
pop_guest = guests.pop()
print(f"Im sorry, you cant come {pop_guest}")
pop_guest = guests.pop()
print(f"Im sorry, you cant come {pop_guest}")
pop_guest = guests.pop()
print(f"Im sorry, you cant come {pop_guest}")

print(f'{guests[0]} and {guests[1]}, you are still invited')
print(f"{len(guests)} is the length of the list")

del guests