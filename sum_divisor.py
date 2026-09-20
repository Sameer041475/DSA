class solution:
    def checkPerfectNumber(self, num):
        #Write your code here...
        total = 0
        for i in range(1,num):
            if num % i == 0:
                total += i
        return total == num