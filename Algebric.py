def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    return 0
class solution:
    def regularAlgebraicExp(self, s):
        st = []
        result = ""
        for c in s:
            if c.isalpha():
                result += c
            elif c == '(':
                st.append(c)
            elif c == ')':
                while st and st[-1] != '(':
                    result += st.pop()
                if st:
                    st.pop()
            else:
                while st and precedence(st[-1]) >= precedence(c):
                    result += st.pop()
                st.append(c)
        while st:
            result += st.pop()
        return result
'''
if __name__ == "__main__":
    s = input().strip()
    sol = solution()
    print(sol.regularAlgebraicExp(s))
'''