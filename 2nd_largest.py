class solution:
    def secLargest(self, s):
        st = set()
        for c in s:
            if c.isdigit():
                st.add(c)   
        if len(st) < 2:
            return -1
        arr = sorted(st)       
        return int(arr[-2])