class solution:
    def sumOfDivisors(self, num):
        #Write your code here...
        A = []
        for i in range(1,num+1):
            if num % i == 0:
                A.append(i)
        return sum(A)

            