line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

lettersToIndex = {
    'a': 0,
    'b': 1,
    'c': 2
}

# A1
# map[0][0]
# lettersToIndex['a']
# map[1][]
map[int(position[1]) - 1][lettersToIndex[position[0].lower()]] = 'x'
# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")