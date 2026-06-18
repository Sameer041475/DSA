class solution:
    def printHourglassPattern(self, n):
        #Write your code here...
       size = 2 * n

       for i in range(size):
            for j in range(size):

                if i == 0 or i == size - 1:
                    print("*", end=" ")

                elif i < n:
                    if j < (n - i) or j >= size - (n - i):
                        print("*", end=" ")
                    else:
                        print(" ", end=" ")

                else:
                    if j < (i - n + 1) or j >= size - (i - n + 1):
                        print("*", end=" ")
                    else:
                        print(" ", end=" ")

            print()