# states_of_america = ["Delaware", "Pennsylvania"]
# print(states_of_america[0])
# states_of_america[0] = "Colorado"
# states_of_america.append("Alaska")
# print(states_of_america)

import random
# names_string = input()
names_string = "Angela, Ben, Dima, Anastasia, Kate, Olha, Sam"
names = names_string.split(", ")
# payer_name = random.choice(names)
random_int = random.randint(0, len(names)-1)
print(names[random_int])
