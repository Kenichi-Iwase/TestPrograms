# Calculate f(x)=0 by Newton Method
# f(x)を定義
f <- function (x) {
    exp(x) - 2
}
# 範囲をc(0, 1)で指定
result1 <- uniroot(f, c(0, 1))

g <- function(x) {
    x^2 - 3
}
result2 <- uniroot(g, c(1, 3))

h <- function(x) {
    x^2 - 2*x
}
result3 <- uniroot(h, c(1, 3))
