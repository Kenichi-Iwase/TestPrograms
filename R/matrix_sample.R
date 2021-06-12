行列の定義
x <- matrix(1:6, nrow=2, ncol=3)
y <- matrix(1:6, nrow=2, ncol=3, byrow=T)

p1 <- x * y         # 要素ごとの掛け算
p2 <- x %*% t(y)    # 行列の積　転置行列を使用
p3 <- x %o% y       # 外積
p4 <- x %x% y       # クロネッカー積
