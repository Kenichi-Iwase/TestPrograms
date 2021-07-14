# initialize
x_vec = c()
y_vec = c()

# calculate
for (i in 1:50000) {
    x <- runif(1, min=-2, max=2)
    y <- runif(1, min=-2, max=2)

    if (is_in_ellipse(x, y) == 1) {
        x_vec = c(x_vec, x)
        y_vec = c(y_vec, y)
    }
}

x_1 = seq(-2,2,by=0.1)
y_1 = seq(-2,2,by=0.1)
x_2 = seq(-2,2,by=0.1)
y_2 = seq(2,-2,by=-0.1)

plot(x_vec, y_vec,xlab="",ylab="",pch=16,col="blue")
par(new=T)
plot(x_1,y_1,xlab="",ylab="",type="l")
par(new=T)
plot(x_2,y_2,xlab="x", ylab="y", type="l")
title("Graph of ellipse")
