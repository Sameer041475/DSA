class solution:
    def ProductOfDigits(self, num):
        #Write your code here..
        A1 =[]
        result = 1
        while num > 0:
            A = num % 10
            A1.append(A)
            num = num // 10
        for i in A1:
            result = result * i
        return result
            