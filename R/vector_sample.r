# vector sample 01
x <- c(1.0, 2.0, 3.0, 4.0, 5.0)
print("Result of vector x")
print(x)
print("Result of sqrt(x)")
print(sqrt(x))
print("Result of log(x)")
print(log(x))

# vector sample 02
x <- c(0, 1, 4, 9, 16, 25)
print("Result of mean(x)")
print(mean(x))

# vector sample 03
y <- c(1, 2, 3, 4)
z <- c(0, 5, 7, 9)
print("Result of corelation by Pearson")
print(cor(y, z, method="pearson"))
print("Result of corelation by Spearman")
print(cor(y, z, method="spearman"))

# vector sample 04
x <- c(1, 2, 3, 4, 5)
print("Show element 2")
print(x[2])
x[4] <- 0
print("Replace")
print(x)
print("Concatenate")
print(c(x, 4))

# vector sample 05
a <- c(1, 2, 3) + c(4, 5, 6)
print("Add 2 vectors")
print(a)
b <- c(1, 2, 3) * c(4, 5, 6)
print("Produce 2 vectors")
print(b)
c <- c(1.0, 2.0, 3.0, 4.0, 5.0) - 1
print("Subtract all elements")
print(c)

# vector sample 06
x <- 1:5
print("Increment vector")
print(x)
y <- 3:-3
print("Decrement vector")
print(y)

# vector sample 07
a <- seq(1, 5, length=3)
print("Result of seq(1, 5, length=3)")
print(a)
a <- seq(1, 5, by=2)
print("Result of seq(1, 5, by=2)")
print(a)
a <- rep(1:5, times=3)
print("Result of rep(1:5, times=3)")
print(a)
a <- rep(1:10, 3)
print("Result of rep(1:10, 3)")
print(a)
a <- numeric(7)
print("Result of numeric(7)")
print(a)
x <- c(1, 3, 2, 1, 4, 5, 1, 4, 3, 2)
a <- unique(x)
print("Result of unique(x)")
print(a)
