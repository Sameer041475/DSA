class solution:
    def calculateDigitSum(self,N1, N2):
        #Write your code here...
        total = 0
        for i in range(N1, N2+1):
            temp = i
            while temp > 0:
                total += temp % 10
                temp = temp // 10
        return total       
        