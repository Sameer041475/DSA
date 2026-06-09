class solution:
    def countChar(self, str, ch):
        #Write your code here...
        count = 0
        for i in str:
          if i == ch:
              count += 1
        return count