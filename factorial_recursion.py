def find_unique_arrangements(n):
    if n == 0 or n == 1:
        return 1
    return(n * find_unique_arrangements(n-1))