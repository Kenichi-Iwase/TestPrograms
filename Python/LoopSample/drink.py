# define list
drink = ['coffee', 'tea', 'juice', 'milk']

# simple for statement
for x in drink:
    print(x)

# using enumerate function
for i, x in enumerate(drink):
    print(i, x)

# using enumerate function
#   start value = 1
for i, x in enumerate(drink, 1):
    print(i, x)

# using range function
for i in range(len(drink)):
    print(i+1, drink[i])

# define set
drink = {'coffee', 'tea', 'juice', 'milk'}

# using enumerate function
for i, x in enumerate(drink, 1):
    print(i, x)

# simple for statement
i = 1
for x in drink:
    print(i, x)
    i += 1
