class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        st=[]
        for ast in asteroids:
            while st and ast<0<st[-1]:
                if -ast>st[-1]:
                    st.pop()
                    continue
                if -ast==st[-1]:
                    st.pop()
                break
            else:
                st.append(ast)
        
        return st
            
        