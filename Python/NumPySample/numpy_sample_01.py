import numpy as np

print('Vector Sample')
x = np.array([1.0, 2.0, 3.0])
print(x)
print(type(x))

print('Calculate arrays')
y = np.array([2.0, 4.0, 6.0])
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print('Broadcast')
print(x / 2.0)

print('Matrix Sample')
A = np.array([[1, 2], [3, 4]])
print(A)
print(A.shape)
print(A.dtype)

print('Calculate matrix')
B = np.array([[3, 0], [0, 6]])
print(A + B)
print(A * B)
print('Broadcast')
print(A * 10)

print('Broadcast Sample')
B = np.array([10, 20])
print(A * B)

