# Working with Part of a List
# Slicing a List
# Taking items from the zero element to the 3rd element
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

# This will take the second, third, and fourth items
# This print is still pulling from the above list
print(players[1:4])

# You can also leave out the first index, and it will start at zero automatically
print(players[:4])

# You can also leave out the end index, and it will automatically end at the list end
print(players[2:])

# You can also use the negative index to get items from the end of the list
print(players[-3:])

# Looping through a Slice
# This will loop through players[] and output the first three names
print("Here are the first three players on my team:")
# Since we are starting at the beginning, we do not need the first index
for player in players[:3]:
    print(player.title())
