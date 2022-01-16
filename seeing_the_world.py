places = ['Toronto', 'New York', 'Oslo', 'Bali', 'Bora Bora']
print(places)

print(f"\n{sorted(places)}")
print(f"\n{places}")

places.reverse()
print(places)
places.reverse()
print(places)

places.sort()
print(places)

places.sort(reverse=True)
print(places)

games = ['League of Legends', 'Counter Strike', 'Fifa', 'Day Of Defeat', 'Spyro']

games.sort()
print(f"\n")
print(games)

games.sort(reverse=True)
print(f"\n")
print(games)

games.append('Call of duty')
print(f"\n")
print(games)

games.insert(3, 'Nytt Spill')
print(f"\n")
print(games)

childhood_game = games.pop(0)
print(f"\n")
print(sorted(games))
print(f"My childhood game was: {childhood_game}")