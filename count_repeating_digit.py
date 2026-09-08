class solution:
    def countRepeatingDigits(self, num):
        #Write your code here...
        s = str(num)
        count = 0
        for i in range(10):
            if s.count(str(i)) > 1:
                count += 1
        return count