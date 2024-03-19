import random

# random_integer = random.randint(1, 10)
# print(random_integer)

#
# random_float = random.random() * 5
# print(random_float)

random_numbers = random.random()

if round(random_numbers) == 0 :
    print('Heads')
if round(random_numbers) == 1 :
    print("Tails")