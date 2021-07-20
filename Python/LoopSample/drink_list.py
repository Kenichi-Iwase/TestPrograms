# define list
drink = ['coffee', 'tea', 'juice', 'milk', 'coke', 'water']

# simple for statement
print('simple for statement')
for x in drink:
    print(x)

# using enumerate function
print('using enumerate function #1')
for i, x in enumerate(drink):
    print(i, x)

# using enumerate function
#   start value = 1
print('using enumerate function #2')
for i, x in enumerate(drink, 1):
    print(i, x)

# using range function
print('using range function')
for i in range(len(drink)):
    print(i+1, drink[i])
