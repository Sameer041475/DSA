class solution:
    def canFormPalindrome(self, s, t): 
        A = s + t
        A1 = {}
        for i in A:
          if i in A1:
              A1[i] += 1
          else:
              A1[i] = 1
        odd = 0

        for count in A1.values():
            if count % 2 != 0:
                odd += 1

        if odd <= 1:
            return "YES"
        else:
            return "NO"