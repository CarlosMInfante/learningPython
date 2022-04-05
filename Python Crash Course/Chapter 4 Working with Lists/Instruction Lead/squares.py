squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

# A more concise version of above code
squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

# Even more concise version of above code
squares = [value**2 for value in range(1, 11)]
print(squares)
