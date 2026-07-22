class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        ops={
            '+':lambda a,b:a+b,
            '-':lambda a,b:a-b,
            '*':lambda a,b:a*b,
            '/':lambda a,b:int(a/b) if a*b>0 else - (abs(a)//abs(b))
        }

        for token in tokens:
            if token in ops:
                b=st.pop()
                a=st.pop()
                st.append(ops[token](a,b))
            else:
                st.append(int(token))
        return st[0]
         