class solution:
    def checkAutomorphicNumber(self, num):
        #Write your code here...
        square = num * num 
        return str(square).endswith(str(num))