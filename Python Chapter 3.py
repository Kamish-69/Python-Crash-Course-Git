### Chapter 3

## Page 34-35 - Accessing Elements in a List + Playing with Index Positions
fruits = ['mango', 'watermelon', 'apple', 'guava']
print(fruits)
print(fruits[0])
print(fruits[0].title())
print(fruits[-2].capitalize())


## Page 35 - Using individual values like variables
msg1 = f"\nI like {fruits[-4].title()}es."
print(msg1)


## TIY Page no 36

# TIY 3-1 and 3-2 together
names = ['football', 'soccer', 'english', 'harry potter']
print(f"\nI like {names[0].title()} or for Americans, {names[-2].capitalize()}.")
print(f"{names[2].capitalize()} has always been my strong subject \never since reading {names[-1].title()}. ")

# TIY 3-3
vehicle = ['car', 'plane', 'train']
print(f"\n{vehicle[0].title()}s run on roads.")
print(f"{vehicle[-2].capitalize()}s fly.")
print(f"I like {vehicle[2]}s.")


## Modifying, Adding and Removing Elements in a list

# Modifying Elements
fruits = ['mango', 'watermelon', 'apple', 'guava']
print(fruits)
fruits[-1] = 'pear'
print(fruits)

# Adding(appending?) Elements
fruits = ['mango', 'watermelon', 'apple', 'pear']
print()
print(fruits)
fruits.append('pineapple')
print(fruits)

# Inserting Elements
fruits = ['mango', 'watermelon', 'apple', 'pear']
print()
print(fruits)
fruits.insert(4,'strawberry')
print(fruits)

# Removing Elements
print()
print(fruits)
del fruits[4]
print(fruits)

# Popping Elements
fruits = ['mango', 'watermelon', 'apple', 'pear']
print()
print(fruits)
popped_fruit = fruits.pop()
print(fruits)
print(popped_fruit)

# Popping Elements from any position
fruits = ['mango', 'watermelon', 'apple', 'pear']
print()
print(fruits)
popped_fruit = fruits.pop(-1)
print(fruits)
print(f"The last fruit in the list was a {popped_fruit}.")

# Removing Elements by value
things = ['pencil','pen', 'box']
print()
print(things)
things.remove('box')
print(things)

# Removing and working with the value being removed
things = ['pencil','pen', 'box']
print()
print(things)
too_expensive = 'box'
things.remove(too_expensive)
print(things)
print(f"\n{too_expensive.capitalize()} is too expensive for me.")


## TIY PAGE NO 42-43

# TIY 3-4
people = ['a', 'b', 'c']
print()
print()
print()
print(f"\n\t{people[0].title()}, it would be amazing to have you over\n\tfor dinner..5 PM will be perfect!")
print(f"\n\t{people[-2].title()}, it would be amazing to have you over\n\tfor dinner.. 5 PM will be perfect!")
print(f"\n\t{people[2].capitalize()},it would be amazing to have you over\n\tfor dinner..5 PM will be perfect!")

# TIY 3'5
people = ['a', 'b', 'c']
print()
print()
print()
print(f"\n\t{people[0].title()}, it would be amazing to have you over\n\tfor dinner..5 PM will be perfect!")
print(f"\n\t{people[-2].title()}, it would be amazing to have you over\n\tfor dinner.. 5 PM will be perfect!")
print(f"\n\t{people[2].capitalize()},it would be amazing to have you over\n\tfor dinner..5 PM will be perfect!")
print()
print(f"\n\tOh no, looks like {people[1].title()} won't be able to make it")
people[1] = 'D'
print(f"\n\t{people[0].title()}, why don't you come over for dinner?")
print(f"\n\t{people[1].title()}, why don't you come over for dinner?")

