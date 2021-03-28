import numpy

# define vector x
x = numpy.array([1.0, 2.0, 3.0])
print(x)

# define vector y
y = numpy.array([2.0, 4.0, 6.0])
print(y)

# add vector
z = x + y
print(z)

# subtract vector
z = x - y
print(z)

# element-wise product
z = x * y
print(z)

# element-wise division
z = x / y
print(z)

# broadcast
z = x / 2.0
print(z)

# matrix
A = numpy.array([[1, 2], [3, 4]])
print(A)
print(A.shape)
print(A.dtype)

X = numpy.array([[1.0, 2.0], [3.0, 4.0]])
print(X)
print(X.shape)
print(x.dtype)

B = numpy.array([[3, 0], [0, 6]])
print(A + B)
print(A * B)
print(A * 10) # broadcast

# broadcast
A = numpy.array([[1, 2], [3, 4]])
B = numpy.array([10, 20])
print(A * B)

# access to elements
X = numpy.array([[51, 55], [14, 19], [0, 4]])
print(X)
print(X[0])     # row 0
print(X[0][1])  # element (0, 1)
print(X[2])     # row 2
print(X[2][0])  # element (2, 0)
print(X[1:])    # row 1 & 2

# using for statement
for row in X:
    print(row)

# X -> one-dimension array
Y = X.flatten()
print(Y)

# extract designated elements
Z = Y[numpy.array([0, 2, 4])]
print(Z)

# extract elements which conditions are true
print(Y > 15)
print(Y[Y>15])
