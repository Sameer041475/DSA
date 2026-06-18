class solution:
    def printButterflyPattern(self, n):
        #Write your code here...
        # Upper half
        for i in range(1, n + 1):
            print("* " * i, end="")
            print("  " * (2 * (n - i)), end="")
            print("* " * i)

        # Lower half
        for i in range(n - 1, 0, -1):
            print("* " * i, end="")
            print("  " * (2 * (n - i)), end="")
            print("* " * i)