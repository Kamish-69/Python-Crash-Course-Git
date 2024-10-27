# TIY P1 of Chapter 2. Page no 25

# An unnecesarily complex way to write a simple sentence
fn= "eric"
ln= "watson"
full_name = f"{fn.title()} {ln.title()}"
msg = f"Hello {full_name}, \nwould you like to learn some Python today?"
print(msg)

# Printing Eric Watson in 3 different ways
name = "eric watson"
print(name.title())
print(name.upper())
print(name.lower())

# Two ways to quote Albert Einstein
print('\tAlbert Einstein once said, "A person who never made a \n\tmistake never tried anything new." ')

famous_name = "albert einstein"
message = f'\t{famous_name.title()} once said,"A person who never made a \n\tmistake never tried anything new."'
print(message)

# Sherlock Holmes but im removing spaces
name = "   sherlock holmes   "
msg = f"\n\t{name.title()}"
print(msg)
print(msg.lstrip())
print(msg.rstrip())
print(msg.strip())


# TIY P2 of Chapter 2 Page 29-30

# Four print commands which result in 8
print(4+4)
print(4*2)
print(2 ** 3)
print(3 + 5)

# My favourite number
NUM = 7
print(f"My favourite number is {NUM}")





