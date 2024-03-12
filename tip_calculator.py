print('Welcome to the tip calculator!')
bill = 15float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, 15 "))
number_of_people = int(input("How many people to split the bill?"))
tip_value = tip / 100 + 1
cost = round((bill / number_of_people) * tip_value,2)
print(f"Each person should pay {cost} $")