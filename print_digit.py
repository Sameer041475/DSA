class solution:
    def printDigit(self, n):
        #Write your code here...
        while n > 0:
            digit = n % 10
            print(digit)
            n = n // 10
        
            