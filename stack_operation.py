class solution:

    def push(self, s, x):
        # Write your code here...
        s.append(x)

    def pop(self, s):
        # Write your code here...
        if s:
            return s.pop()
        return -1

    def isEmpty(self, s):
        # Write your code here...
        return len(s) == 0
    def getMin(self, s):
        # Write your code here...
        if s:
            return min(s)
        return -1
    