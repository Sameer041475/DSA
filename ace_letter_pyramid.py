class solution:
    def printAscLetterPyramid(self, n):
        #Write your code here...
         for i in range(1, n + 1):
            start = 65 + (n - i)

            for j in range(i):
                print(chr(start + j), end=" ")
            print()