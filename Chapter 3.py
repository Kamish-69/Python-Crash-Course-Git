### Chapter 3

## Page 34-35 - Accessing Elements in a List + Playing with Index Positions
fruits = ['mango', 'watermelon', 'apple', 'guava']
print(fruits)
print(fruits[0])
print(fruits[0].title())
print(fruits[-2].capitalize())


## Page 35 - Using individual values like variables
msg = f"\nI like {fruits[-4].title()}es."
print(msg)


## TIY Page no 36

# TIY 3-1 and 3-2 together
names = ['football', 'soccer', 'english', 'harry potter']
print(f'\nI like playing {names[0]}, or for Americans, "{names[-3].lower()}".')
print(f"\n{names[2].capitalize()} has always been my strong subject \never since reading {names[-1].title()}. ")

# TIY 3-3
vehicle = ['car', 'plane', 'train']
print(f"\n{vehicle[0].title()}s run on roads.")
print(f"{vehicle[-2].capitalize()}s fly.")
print(f"I like {vehicle[2]}s.")        # I don't have any actual "liking" to trains in particular,
                                       #     I just couldn't think of what to write. (Wow, I just found out- it's a meme??!!)


## Modifying, Adding and Removing Elements in a list

# Modifying Elements
print("\n\nModifying Elements:")
fruits = ['mango', 'watermelon', 'apple', 'guava']
print(fruits)
fruits[-1] = 'pear'
print(fruits)

# Adding("Appending") Elements
print("\nAdding/Appending Elements:")
fruits = ['mango', 'watermelon', 'apple', 'pear']
print(fruits)
fruits.append('pineapple')
print(fruits)

# Inserting Elements
fruits = ['mango', 'watermelon', 'apple', 'pear']
print('\nInserting Elements:')
print(fruits)
fruits.insert(3,'strawberry')
print(fruits)

# Removing Elements
fruits = ['mango', 'watermelon', 'apple', 'strawberry', 'pear']
print('\nRemoving Elements:')
print(f'{fruits}')
del fruits[4]
print(fruits)

# Popping Elements
fruits = ['mango', 'watermelon', 'apple', 'pear']
print('\nPopping Elements:')
print(fruits)
popped_fruit = fruits.pop()
print(fruits)
print(popped_fruit)

# Popping Elements from any position
fruits = ['mango', 'watermelon', 'apple', 'pear']
print('\nPopping Elements from any position:')
print(fruits)
popped_fruit = fruits.pop(-4)
print(fruits)
print(f"The first fruit in the list was a {popped_fruit}.")

# Removing Elements by value
things = ['pencil','pen', 'box']
print('\nRemoving Elements by value:')
print(things)
things.remove('box')
print(things)

# Removing and working with the value being removed
things = ['pencil','pen', 'box']
print('\nRemoving and working with the value being removed:')
print(things)
too_expensive = 'box'
things.remove(too_expensive)
print(things)
print(f"\t{too_expensive.capitalize()} is too expensive for me.")


## TIY PAGE NO 42-43

# TIY 3-4
people = ['a', 'b', 'c']
print()
print()
print()
print(f"\n\t{people[0].title()}, it would be amazing to have you over\n\tfor dinner..5 PM will be perfect!")
print(f"\n\t{people[-2].title()}, it would be amazing to have you over\n\tfor dinner.. 5 PM will be perfect!")
print(f"\n\t{people[2].capitalize()},it would be amazing to have you over\n\tfor dinner..5 PM will be perfect!")

# TIY 3-5
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
print(f"\n\t{people[2].title()}, why don't you come over for dinner?")


        # Variation of TIY 3-5 with Popping  (From the Future)     Note - Notes from the future will have '-F' at the end   -F
people = ['a', 'b', 'c']
print(f"\n\n\n\n\t{people[0].title()}, it would be amazing to have you over\n\tfor dinner..5 PM will be perfect!")
print(f"\n\t{people[-2].title()}, it would be amazing to have you over\n\tfor dinner.. 5 PM will be perfect!")
print(f"\n\t{people[2].capitalize()},it would be amazing to have you over\n\tfor dinner..5 PM will be perfect!")
boring_person = 'b'
people.remove(boring_person)
print(f"\n\n\tAh, looks like {boring_person.title()} won't be able to make it...")
people.insert(1,'D')
print(f"\n\t{people[0].title()}, come over for dinner!")
print(f"\n\t{people[1].title()}, come over for dinner!")
print(f"\n\t{people[-1].title()}, come over for dinner!")

        # Hmm, seems good... Back to present   -F

# TIY 3-6 and 3-7
people = ['a', 'b', 'c']
print()
print()
print()
print("\nOh, would you look at that! I found a bigger dining table for 69$. I'll be inviting a few more people :)")
people.insert(0,'Z')
people.insert(2,'E')
people.append('F')
print(f"\n\t{people[0].title()}, Why don't we have dinner together tonight? Come over.")
print(f"\n\t{people[1].title()}, why don't we have dinner together tonight? Come over.")
print(f"\n\t{people[2].title()}, why don't we have dinner together tonight? Come over.")
print(f"\n\t{people[3].title()}, why don't we have dinner together tonight? Come over.")
print(f"\n\t{people[4].title()}, why don't we have dinner together tonight? Come over.")
print(f"\n\t{people[5].title()}, why don't we have dinner together tonight? Come over.")

print("\nOh no, the dinner table won't be arriving on time and  I can only invite two people")
pop_person = people.pop()
print(f"\n{pop_person.title()}, I'm really sorry, but looks like I won't be able to invite you for dinner")
pop_person = people.pop()
print(f"\n{pop_person.title()}, I'm really sorry, but looks like I won't be able to invite you for dinner")
pop_person = people.pop()
print(f"\n{pop_person.title()}, I'm really sorry, but looks like I won't be able to invite you for dinner")
pop_person = people.pop()
print(f"\n{pop_person.title()}, I'm really sorry, but looks like I won't be able to invite you for dinner")
print(f'\n\n{people}')
print(f"\n{people[0].title()}, Come over to dinner! You're still invited")
print(f"{people[1].title()}, Come over to dinner! You're still invited")
del people[0]
del people[0]
print(people)

## TIY Page 46

# TIY 3-8
places = ['library','hill station','mountains','place4','place5']
print()
print()
print()
print(places)
print()
print(sorted(places))
print()
print(places)
print()
print(sorted(places, reverse=True))
print()
print(places)
print()
places.reverse()
print(places)
print()
places.reverse()
print(places)
print()
places.sort()
print(places)
print()
places.sort(reverse=True)
print(places)
print()

# TIY 3-9
people = ['a', 'b', 'c']
print()
people.insert(0,'d')
people.insert(2,'e')
people.append('f')
people_invited = len(people)
print(f"I'm inviting a total of {people_invited} people.")

# TIY 3-10
# THIS PROGRAM USES EVERY FUNCTION IN THIS CHAPTER (hopefully)
mountains = ['Everest','Etna','Kanchenjunga']
print()
print()
print()
print(mountains)
print(mountains[0])
print(mountains[-1].upper())
msg = f"Mt {mountains[0].title()} is the tallest mountain in the world."
print(msg)
mountains[2] = 'Vesuvius'
print(mountains)
mountains.append('Kanchenjunga')
print(mountains)
mountains.insert(0,'Otto')
print(mountains)
del mountains[0]
print(mountains)
popped_mountain = mountains.pop(0)
print(f"Mt {popped_mountain} was just popped.")
print(mountains)
mountains.remove('Etna')
print(mountains)
beautiful = 'Kanchenjunga'
mountains.remove(beautiful)
print(f"Mt {beautiful.title()} is a beautiful mountain.")
print(mountains)
mountains.append('Kanchenjunga')
mountains.append('Everest')
mountains.append('Etna')
print(mountains)
print(sorted(mountains))
print(sorted(mountains, reverse=True))
mountains.sort()
print(mountains)
mountains.sort(reverse=True)
print(mountains)
mountains.reverse()
print(mountains)
mountains.reverse()
print(mountains)
print(len(mountains))
