def add2(x, y):
    return x + y

def sub2(x, y):
    return x - y

def mul2(x, y):
    return x * y

def div2(x, y):
    if y == 0:
        return 0
    else:
        return x / y

def divi2(x, y):
    if y == 0:
        return 0
    else:
        return x // y

print(add2(3, 2))
print(sub2(3, 2))
print(mul2(3, 2))
print(div2(3, 2))
print(divi2(3, 2))
