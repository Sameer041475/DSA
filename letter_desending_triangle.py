class solution:
    def printDescendingLetterTriangle(self, n):
        #Write your code here...
        
        
        for i in range(n,0,-1):
            for j in range(i):
                print(chr(65+j),end = " ")
            print()