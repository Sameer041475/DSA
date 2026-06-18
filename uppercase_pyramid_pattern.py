class solution:
    def printUppercaseLetterPyramid(self, n):
        #Write your code here...
        
        

        for i in range(1, n + 1):
            # spaces
            print(" " * (n - i), end="")
    
            # ascending letters
            for j in range(i):
                print(chr(65 + j), end="")
    
            # descending letters
            for j in range(i - 2, -1, -1):
                print(chr(65 + j), end="")
    
            print()