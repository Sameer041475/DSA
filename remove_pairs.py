class solution:
    def cleanString(self, s):
        # Write your code here...
        while "ab" in s or "AB" in s:
            s = s.replace("ab", "")
            s = s.replace("AB", "")
            return s