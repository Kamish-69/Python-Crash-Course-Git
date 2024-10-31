### Chapter 5 - If Statements

# A Simple Example
cars = ['ferrari','audi','bmw','toyota']
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

# Elif
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


