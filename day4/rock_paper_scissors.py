import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

art = [rock, paper, scissors]

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors ")
person_choice = int(input())
computer_choice = random.randint(0, 2)
print(f'{art[person_choice]}\n{art[computer_choice]}')


if (((person_choice == 0 and computer_choice == 0) or
        (person_choice == 1 and computer_choice == 1)
        or (person_choice == 2 and computer_choice == 2)) or
        (person_choice == 3 and computer_choice == 3)):
    print("It's a draw")

elif person_choice == 0 and computer_choice == 1:
    print("Computer won")
elif person_choice == 0 and computer_choice == 2:
    print("Computer lose")

elif person_choice == 1 and computer_choice == 0:
    print("Computer lose")
elif person_choice == 1 and computer_choice == 2:
    print("Computer won")
elif person_choice == 2 and computer_choice == 1:
    print("Computer lose")
elif person_choice == 2 and computer_choice == 0:
    print("Computer won")



