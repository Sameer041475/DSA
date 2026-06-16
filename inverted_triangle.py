class solution:
    def printInvertedRightAngledTrianglePattern(self, n):
        #Write your code here...
        for i in range(0,n):
            A1 = ("* " * (n-i))
            print(A1)