class solution:
    def kthDigit(self,A, B, k):
        #Write your code here...
        A1 = A ** B
        A2 = str(A1)
        return A2[-k]