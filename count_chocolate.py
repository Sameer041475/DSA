class solution:
    def countChocolates(self, s):
      #Write Your Code Here...
        b=''
        count=0
        for i in s:
            if i not in b:
                count+=2
                b+=i
            else:
                count+=1
        
        return(count)
            