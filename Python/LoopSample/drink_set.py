# define set
drink = {'coffee', 'tea', 'juice', 'milk', 'coke', 'water'}

# using enumerate function
print('using enumerate function')
for i, x in enumerate(drink, 1):
    print(i, x)

# simple for statement
print('simple for statement')
i = 1
for x in drink:
    print(i, x)
    i += 1
