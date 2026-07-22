class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st=[]
        for c in operations:
            if c=='+':
                el=st[-1]+st[-2]
                st.append(el)
            elif c=='C':
                st.pop()
            elif c=='D':
                el=2*st[-1]
                st.append(el)
            else:
                st.append(int(c))
                
        return sum(st)

        