class solution:
    def manipulateArray(self, arr, n, k):
        arr[(n - 1) // 2] *= k
        print(*arr)