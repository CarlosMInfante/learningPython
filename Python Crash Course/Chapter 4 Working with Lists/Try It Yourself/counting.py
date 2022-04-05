# Use a for loop to count to 20
for i in range(21):
    print(i)

# One Million
i = []
for value in range(1000001):
    i.append(value)
print(min(i))
print(max(i))
print(sum(i))

# Odd Numbers:
for value in range(1, 21, 2):
    print(value)

# Threes:
for value in range(3, 30, 3):
    print(value)

# Cubes:
for value in range(1, 21):
    value.append(value**3)
    print(value)

# Cube Compression:
cubes = []
for value in range(1, 11):
    cubes.append(value**3)
print(cubes)
