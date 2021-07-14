is_in_ellipse <- function (x, y) {
    if( 3.0*x^2 - 2.0*x*y + 3.0*y^2 - 8.0 < 0) {
        return(1)
    }
    else {
        return(0)
    }
}
