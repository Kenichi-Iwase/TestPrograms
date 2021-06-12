# 最小二乗法の切片と傾きを求める関数 min.sq
min.sq <- function(x, y) {
    x.bar <- mean(x)
    y.bar <- mean(y)
    beta.1 <- sum((x-x.bar)*(y-y.bar))/sum((x-x.bar)^2)
    beta.0 <- y.bar - beta.1 * x.bar
    return(list(a=beta.0, b=beta.1))
}

# 直線の係数をランダムに生成
a <- rnorm(1)
b <- rnorm(1)

# 直線の周りの点をランダムに生成
N <- 100;
x <- rnorm(N)
y <- a * x + b + rnorm(N)

# 点のプロット
plot(x, y)
abline(h=0)
abline(v=0)

# 中心化前の直線
abline(min.sq(x,y)$a, min.sq(x,y)$b, col="red")

# 中心化
x <- x - mean(x)
y <- y - mean(y)

# 中心化後の直線
abline(min.sq(x,y)$a, min.sq(x,y)$b, col="blue")

# 凡例
legend("topleft", c("before centering", "after centering"), lty=1, col=c("red", "blue"))
#legend("topleft", c("中心化前", "中心化後"), lty=1, col=c("red", "blue"))
