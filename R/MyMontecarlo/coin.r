# コイントス
coin <- function() {
    x <- runif(1)
    if (x <= 1/2) {
        men <- 1
    }
    else {
        men <- 0
    }

    return(men)
}
