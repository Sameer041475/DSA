class solution:
    def sumOfDiagonals(self, matrix, n):
        #Write your code here...
        primary = 0
        secondary = 0

        for i in range(n):
            primary += matrix[i][i]
            secondary += matrix[i][n - 1 - i]

        print(primary, secondary)