bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[2].title(),bicycles[0].title())
print(f"Min favoritt sykler er {bicycles[1].title()} og {bicycles[2].title()}")

names = ['Berat', 'Abdul', 'Louise', 'Mariam']
popped_name = names.pop()
print(names)
del names[1]
print(names)
print(f"Siste personen i lista er {popped_name}")

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive} is too expensive for me.")




