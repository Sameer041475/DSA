class solution:
    def printAlternatingBinaryTriangle(self, n):
        #Write your code here...
        
        for i in range(1, n+1):
            for j in range(0, i):
                print((i + j) % 2, end=" ")
            print()
        