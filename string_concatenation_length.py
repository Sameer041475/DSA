class solution:
    def lengthAfterConcat(self, n, arr):
        s = ""
        for word in arr:
            s += word
        return len(s)