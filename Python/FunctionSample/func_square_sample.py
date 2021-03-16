# calculate square by function

def square(x):
    return x ** 2

# calculate square
result = square(3)
print(result)

# calculate square from list
data = [1, 2, 3, 5, 9, 12]
for i, x in enumerate(data):
    print(square(x))
    print(square(data[i]))
