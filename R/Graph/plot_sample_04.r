# plot sample 04
gauss.density <- function(x) {
    1 / sqrt(2 * pi) * exp(-x^2 / 2)
}
plot(gauss.density, -3, 3)
