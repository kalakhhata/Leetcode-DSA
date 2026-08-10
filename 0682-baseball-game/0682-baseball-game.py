class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st=[]

        for ops in operations:
            if ops=='C':
                if st:
                    st.pop()
            elif ops=='D':
                if st:
                    el=st[-1]
                    st.append(el*2)
            elif ops=='+':
                el1=st[-1]
                el2=st[-2]
                st.append(el1+el2)
            else:
                st.append(int(ops))
        
        return sum(st)
        