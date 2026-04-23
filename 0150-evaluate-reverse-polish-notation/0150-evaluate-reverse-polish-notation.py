class Solution(object):
    def evalRPN(self, tokens):
        st = []

        ops = {
            '+': lambda a,b: a + b,
            '-': lambda a,b: a - b,
            '*': lambda a,b: a * b,
            '/': lambda a,b: int(a / b) if a * b > 0 else - (abs(a) // abs(b))
        }

        for t in tokens:
            if t in ops:
                b = st.pop()
                a = st.pop()
                st.append(ops[t](a, b))
            else:
                st.append(int(t))

        return st[-1]