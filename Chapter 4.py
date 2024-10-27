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