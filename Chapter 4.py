##### Chapter 4 - Working with Lists
# Note - TIY stands for Try it Yourself exercises

# uhh, loops?
people = ['david','alex','thomas','Michael']
for person in people:
    print(person.title())
    print()
for person in people:
    print(f"{person.title()} is a good person.")

performers = ['david','alex','thomas','Michael']
print()
for performer in performers:
    print(f"{performer.title()}, that was an excellent performance!")
    print(f"\tI can't wait to see the next part, {performer.title()}.")
print()
print("All of you did amazing, guys! Keep it up.")

## TIY Page 56
# TIY 4-1
pizzas = ['pizza1','pizza2','pizza3']
for pizza in pizzas:
    print(f"I like {pizza}.")
print(f"I really love pizza.")

# TIY 4-2
birds = ['parrot','hummingbird','crow']
print()
for bird in birds:
    print(f"{bird.title()}s can fly.")
print("\tAll these animals are birds!")


# Testing range() function
for value in range(1,9):
    print(value)
print()
for value in range(9):
    print(value)

# Using range() to make a list of numbers
cubes = []
for number in range(1,11):
    cube = number ** 3
    cubes.append(cube)
print(f"\n{cubes}")

cubes = []
for value in range(1,11):
    cubes.append(value ** 3)
print(cubes)

# Simple Statistics
print()
print(min(cubes))
print(max(cubes))
print(sum(cubes))

# List Comprehensions
squares = [value ** 2 for value in range(1,11)]
print(f"\n{squares}")

## TIY Page 60

# TIY 4-3
print()
for value in range(1,21):
    print(value)

# TIY 4-5
print()
million = []
for value in range(1,1000001):
    million.append(value)
print(min(million))
print(max(million))
print(sum(million))

# TIY 4-6
odd = []
for value in range(1,21,3):
    odd.append(value)
    print(odd)

# TIY 4-7
print()
threes = list(range(1,31,3))
for value in threes:
    print(value)

# TIY 4-8
print()
cubes = list(range(1,11))
for value in cubes:
    print(value**3)

# TIY 4-9
print()
cubes = [value ** 3 for value in range(1,11)]
print(cubes)

## Working with Part of Lists

# Slicing a List
print()
places = ['New York','Ashburn','Atlanta','Toronto']
print(places[0:2])
print(places[:3])
print(places[1:])

# Looping through a Slice
players = ['David','Max Verstappen','Fernand Alonso','Lewis Hamilton','Sebastian Vettel']
print("\nHere are the last three players in my team")
for player in players[-3:]:
    print(player)

# Copying a List
f1racers = ['Max Verstappen','Fernando Alonso','Lewis Hamilton','Sebastian Vettel']
youngster = f1racers[:1]
print("\n\nSome Formula 1 racers are:")
print(f1racers)
print("\nThe youngest one of these racers is")
print(youngster)

## TIY Page 65

# TIY 4-10
f1racers = ['Max Verstappen','Fernando Alonso', 'Lewis Hamilton','Sebastian Vettel','Michael Schumacher']
print(f"\n\n\nThe first three racers in the list are {f1racers[:3]}")
print("\nThe middle three racers in the list are:")
print(f1racers[1:-1])
print(f"\nThe last three racers in the list are {f1racers[-3:]}")

# TIY 4-11
pizzas = ['pizza1','pizza2','pizza3']
friend_pizzas = pizzas[:]
pizzas.append('pizza4')
friend_pizzas.append('friend_pizza')
print("\n\nMy favourite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("\nMy friend's most liked pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

# TIY 4-12
my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]

print("\n\nMy favourite foods are:")
for food in my_foods:
    print(food)

print("\nNy friend's favourite food are:")
for food in friend_foods:
    print(food)


## Tuples

# Defining a Tuple
dimensions = (15,12,10)
print(f"\n\n\n{dimensions[1]}")

print()
for dimension in dimensions:
    print(dimension)

    # Note - Tuples can't be modified, but we can assign a new value(tuple) to the variable that represents the original tuple, like so:
example_tuple = (37, 37, 37)
print("\n\nOriginal Tuple:")
print(example_tuple)

example_tuple = (11, 12, 13)
print("\nModified Tuple:")
print(example_tuple)


## TIY Page 68

# TIY 4-13
menu = ('Food1','Food2','Food3','Food4','Food5')
print("\n\n\nRestaurant X offers five delicacies, namely: ")
for food in menu:
    print(food)

# menu[0] = 'Pizza'  (this was part of the TIY, attempt to modify the tuple and fail miserably)

menu = ('Ice Cream','Milkshake','Food3','Food4','Food5')
print("\nRestaurant X's revised menu offers:")
for food in menu:
    print(food)



