### Chapter 5 - If Statements

# A Simple Example
cars = ['ferrari','audi','bmw','toyota']

print()
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# Checking for Inequality
requested_topping = 'Pineapple'
served_topping = 'pepperoni'

print(f"\nWaiter - 'Here is your ordered pizza with {served_topping}.'")
if served_topping.lower() != requested_topping.lower():
    print(f"Customer - 'But I wanted {requested_topping.lower()} topping.'")

# Using 'and' to check multiple conditions + Chained Comparisons
Jack = 14
david = 19
if 13 <= Jack <= 19 and 13 <= david <= 19:
    print(f"\n\nJack and David are teenagers.")

# Using 'Elif' function
Jack = 12
david = 15

if 13 <= Jack <= 19 and 13 <= david <= 19:
    print(f"\n\nJack and David are teenagers.")
elif 13 <= Jack <=19:
    print("\nJack is a teenager.")
elif 13 <= david <= 19:
    print("\nDavid is a teenager.")
else:
    print("Neither Jack or David is a teenager")

# Checking whether value in list
requested_topping = 'Pineapple'

if 'pineapple' in requested_topping.lower():
    print("\n\nIt's illegal to put pineapple on pizza.")

# Checking whether value not in list
requested_topping = 'tomato'
illegal_topping = 'pineapple'

if illegal_topping not in requested_topping:
    print(f"\nThank god you didn't ask for {illegal_topping}.")

## TIY Page 78

# TIY 5-1
requested_topping = 'pineapple'
print("\n\n\nDid you request for pineapple? I predict false.")
print(requested_topping == 'pineapple')

print("\nDid you request for pineapple? I predict True")
print(requested_topping == 'pineapple')

print("\nDid you request for pepperoni? I predict false")
print(requested_topping == 'pepperoni')

requested_topping = 'pepperoni'
print("\n Did you request for pepperoni? I predict false")
print(requested_topping == 'pepperoni')

requested_topping = 'tomato'
print("\nDid you request for tomato? I predict true")
print(requested_topping == 'tomato')

print("\nDid you request for tomato? I predict false")
print(requested_topping == 'tomato')

print("\nDid you request for water on your pizza? I predict false")
print(requested_topping == 'water')

print("\nDid you request for water on your pizza? I predict true")
print(requested_topping == 'water')

print("\nDid you request for furniture on your pizza? I predict true")
print(requested_topping == 'furniture')

print('\nDid you request for furniture on your pizza? I predict false')
print(requested_topping == 'furniture')

# TIY 5-2
car = 'ferrari'

if car.lower() == 'ferrari':
    print('\nFerrari indeed is a good car.')

if car.lower() != 'audi':
    print("\nYeah okay, but ferrari is better.")


david = 15
print()
print(13 <= david <= 19)
print(12 >= david >=20)
print(david == 21)
print(david != 21)
print(david > 40)
print(david < 50)

if david >= 13 and david >=19:
    print("\nDavid is a teenager")

if (13 <= david <=19) or (david < 10):
    print('\nDavid is either a teenager or under age of 10')
    # or you can do what is asked and just test instead of printing messages


cars = ['ferrari','audi','bmw','toyota']

if 'ferrari' in cars:
    print(f"\nFerrari is in {cars} list.")
if 'mercedes' not in cars:
    print('Why is Mercedes not in the list?')

    # or you can simply do what is asked like so:-
print('ferrari' in cars)
print('mercedes' not in cars)


# If Statements
age = 19

if age >= 18:
    print("\n\n\nYou are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("\nSorry, you are too young to vote yet.")
    print("Make sure to register so you can vote once you turn 18.")

# The if-elif-else chain  ( which I had learned earlier in the previous chapter from the internet)
age = 21

print("\n")
if age <= 4:
    print("Your admission cost is 0")
elif age < 18:
    print("Your admission cost is 4$")
else:
    print("You admission cost is 70$")

    # A better way to do this
age = 17

if age <=4:
    price = 0
elif age <=18:
    price = 20
else:                           # Note - In cases where you have a specific final condition, consider using a final 'elif' block
    price = 70                  # and omit the else block. Bonus confidence that the code will run only under correct conditions.

print(f"\nYour admission cost is ${price}.")


## TIY Page 84

# TIY 5-3
alien_color = 'green'
print("\n\n")

if alien_color == 'green':
    print("Congratulations , you just earned 5 points!")

alien_color = 'red'

if alien_color == 'green':
    print("Congratulations, you just earned 5 points")


# TIY 5-4
alien_color = 'green'
print("\n")

if alien_color == 'green':
    print("You earned 5 points!")
else:
    print("You earned 10 points!")

alien_color = 'yellow'
print()

if alien_color == 'green':
    print("You earned 5 points!")
else:
    print("You earned 10 points!")


# TIY 5-5
alien_color = 'green'
print("\n")

if alien_color == 'green':
    print("Congrats, you just earned 5 points!")
elif alien_color == 'yellow':
    print("Congrats, you just earned 10 points!")
else:
    print("Congrats, you just earned 15 points!")

alien_color = 'yellow'
print()

if alien_color == 'green':
    print("Congrats, you just earned 5 points!")
elif alien_color == 'yellow':
    print("Congrats, you just earned 10 points!")
else:
    print("Congrats, you just earned 15 points!")

alien_color = 'red'
print()

if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
else:
    print("You just earned 15 points!")

