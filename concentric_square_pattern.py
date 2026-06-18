class solution:
    def printConcentricSquarePattern(self, n):
        #Write your code here...
        size = 2 * n - 1

        for i in range(size):
            for j in range(size):
                top = i
                left = j
                bottom = size - 1 - i
                right = size - 1 - j

                print(n - min(top, left, bottom, right), end=" ")
            print()