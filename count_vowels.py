class solution:
    def countVowels(self, str):
        #Write your code here...
        count = 0
        A = 'aeiouAEIOU'
        for i in str:
            if i in A:
                count += 1
        return count