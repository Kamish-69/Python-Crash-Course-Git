### Chapter 4 - Working with Lists

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

cubes = []
for value in range(1,11):
    cube = value ** 3
    cubes.append(cube)
print(cubes)

cubes = []
for value in range(1,11):
    cubes.append(value ** 3)
print(cubes)
