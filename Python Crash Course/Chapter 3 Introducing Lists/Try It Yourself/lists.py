# Names: Store the names of a few friends in a list called names.  Print each person's name by accessing each element
# in the list, one at a time.
# Greetings: Start with the list you used in Names, but instead of just printing each person's name, print a message
# to them.  The text of each message should be the same, but each message should be personalized with the person's name.
# Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that
# stores several examples.  Use your list to print a series of statements about these items, such as I would like to
# own a Honda motorcycle.

# Names:
names = ['mark', 'sam', 'chris', 'sarah']
print(names[0])
print(names[1])
print(names[2])
print(names[3])

# Greeting:
message = "Hello,"
print(f"{message} {names[0]}")
print(f"{message} {names[1]}")
print(f"{message} {names[2]}")
print(f"{message} {names[3]}")

# Your Own List:
transportation = ['honda', 'toyota', 'mazda', 'ford']
message = "It's nice driving in a"
print(f"{message} {transportation[0]}")
print(f"{message} {transportation[1]}")
print(f"{message} {transportation[2]}")
print(f"{message} {transportation[3]}")
