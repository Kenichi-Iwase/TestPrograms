# plot sample 05
# using curve function
gauss.density <- function(x) {
    1 / sqrt(2 * pi) * exp(-x^2 / 2)
}
curve(gauss.density, -3 , 3)
