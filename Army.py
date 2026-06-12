class solution:
    def isDominant(self, p, q, r):
        if p > q + r or q > p + r or r > p + q:
            return "YES"
        return "NO"