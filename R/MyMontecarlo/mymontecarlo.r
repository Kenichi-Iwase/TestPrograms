mymontecarlo <- function(n) {
    count <- 0
    for (i in 1:n) {
        count <- count + coin()
    }

    return(count/n)
}
