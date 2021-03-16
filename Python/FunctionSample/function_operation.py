
def f(x, y, z):
    return x + y + z

def show_string(str):
    print(str)

def five_adds(a, b, c, d=0, e=0):
    return a + b + c + d + e

result = f(1, 2, 3)
print(result)

show_string("こんにちは。")
show_string("I have a dream.")

result = five_adds(1, 2, 3)
print(result)

result = five_adds(1, 2, 3, 4)
print(result)

result = five_adds(1, 2, 3, 4, 5)
print(result)
