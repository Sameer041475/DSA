class solution:
    def printTrianglePattern(self, n):
        #Write your code here...
        for i in range(1,n):
            A1 = "* " * i
            print(A1)
        
        for j in range(n,0,-1):
            A2 = "* " * j
            print(A2)