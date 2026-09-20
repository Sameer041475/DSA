class solution:
    def secondLargestDigit(self, num):
        #Write your code here...
        digits = sorted(set(str(num)) , reverse = True)
        return int(digits[1])