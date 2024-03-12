
print('Welcome to the BMI calculator')
name = input('Enter your name: ')
height = float(input('Enter your height: '))
weight = float(input('Enter your weight: '))
BMI_index = round(weight / height ** 2)
print(f'{name}, your BMI index is: {BMI_index}')
