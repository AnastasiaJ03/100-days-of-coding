print('Welcome to the roller coaster')
height = int(input('Enter your height in cm '))
if height >= 120:
    print("You can ride the roller coaster!")
    age = int(input("Enter your age :"))
    if age < 12:
        print("You need to pay 5$")
    elif age <= 18:
        print("You need to pay 7$")
    else:
        print("You need to pay 12$")
else:
    print("Sorry , you have to grow taller before you can ride ")

#
# number = int(input('Which number do you want to check?'))

# if number % 2 == 0:
#     print('This is an even number')
# else:
#     print("This is an odd number")