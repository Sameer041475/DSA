class solution:
    def insert(self, q, k):
        #Write your code here...
         q.append(k)
    

    def findFrequency(self, q, k):
        #Write your code here...
        if k in q:
            return q.count(k)
        return -1
    