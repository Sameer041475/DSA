class Solution:
    def insertElement(self, arr, x):
        # Write your code here...
       arr.append(x)
    #   return arr

    def deleteElement(self, arr, x):
        if x in arr:
            arr.remove(x)
    def reverseArray(self, arr):
        # Write your code here...
         arr.reverse()
        

    def sizeOfArray(self, arr):
        # Write your code here...
        print(len(arr))
        # return a4
    def displayArray(self, arr):
        # Write your code here...
        print(*arr)