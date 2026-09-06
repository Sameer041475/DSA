class solution:
    def isPalindrome(self, n):
        org = n
        rev = 0
        while n > 0:
            digit = n % 10 # last digit
            rev = rev * 10 + digit
            n = n // 10
            
        return org == rev
                    