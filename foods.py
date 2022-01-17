my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append("Sucuklu Yumurta")
friend_foods.append("Meatballs")

print("My favorite foods are:")
print(my_foods)

print("\nMy friends' favorite foods are:")
print(friend_foods)

for food in my_foods[:3]:
    print(f"The first three items in the list are: {food}")

print(f"\n")

for food in my_foods[1:3]:
    print(f"Three items from the middle in the list are: {food}")

print(f"\n")

for food in my_foods[-3:]:
    print(f"The last items in list are: {food}")

my_pizzas = ["margherita", "falafel", "pickle", "beef"]
friend_pizzas = my_pizzas[:]

my_pizzas.append("kebab")

for pizza in my_pizzas:
    print(f"My favorite pizzas are: {pizza}")

print(f"\n")

for pizza in friend_pizzas:
    print(f"My friends favorite pizzas are: {pizza}")