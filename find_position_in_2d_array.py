class solution:
    def searchElement(self, arr, n, m, k):
        #Write your code here...
        for i in range(n):
            for j in range(m):
                if arr[i][j] == k:
                    print(i, j)
                    return

        print(-1, -1)