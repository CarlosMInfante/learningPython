# Creating a list.  A collection of items in a particular order.
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# Indexes start with 0
print(bicycles[0])

# You can also use methods on lists
print(bicycles[1].title())

# You can use individual values from a list
message = f"My first bicycle was a {bicycles[2].title()}"
print(message)
