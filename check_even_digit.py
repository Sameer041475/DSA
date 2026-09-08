class solution:
    def checkEvenDigits(self, num):
        #Write your code here...
        
        while num > 0:
            A1 = num % 10
            if A1 % 2 != 0:
                return False
            num = num // 10
        return True