class solution:
    def printDivisors(self, n):
        #Write your code here...
        A = []
        for i in range(1,n+1):
            if n % i == 0:
                A.append(i)
        return A