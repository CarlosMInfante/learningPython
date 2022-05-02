# Using one of the programs from the instruction lead and adding a few lines
# One: Print the first three items
# Two: Print the middle three items
# Three: Print the last three items

my_foods = ['pizza', 'falafel', 'carrot cake', 'mexican', 'ice cream', 'grilled chicken', 'cannoli', 'pineapple']
print(my_foods[:3])
print(my_foods[3:6])
print(my_foods[-3:])

# Starting with original pizza list and making one for a friend
pizzas = ['pepperoni', 'mushrooms', 'sausage']
friend_pizzas = pizzas[:]

# Adding a new pizza to the original list
pizzas.append('garlic')
# Adding a new pizza to friend's list
friend_pizzas.append('onion')

# Looping through the list to print all the items
# This will include the appended list because where it falls in the flow
for pizza in pizzas:
    print(pizza)

for friend_pizza in friend_pizzas:
    print(friend_pizza)
