
def my_sqrt(x: int) -> int:
    start = 0
    end = x
    while start <= end:
        n = int((start+end)/2)
        square_n = n*n
        if square_n == x:
            return n
        elif square_n > x:
            end = n-1
        else:
            start = n+1
    return end
