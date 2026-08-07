class solution:
    def hasThreeSumEndingWithThree(self, arr):
        n = len(arr)

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if (arr[i] + arr[j] + arr[k]) % 10 == 3:
                        return "YES"

        return "NO"