class solution:
    def checkHarshadNumber(self, num):
        #Write your code here...
        org = num
        total = 0
        while num > 0 :
            digit = num % 10
            total += digit
            num = num // 10
        if org % total == 0:
            return True
        else:
            return False