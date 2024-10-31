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

