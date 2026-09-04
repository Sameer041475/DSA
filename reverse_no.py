class solution:
    def reverseNumber(self, N):
        #Write your code here...
        rev = 0
        while N > 0:
            digit = N % 10
            rev = rev * 10 + digit
            N = N // 10
        return rev