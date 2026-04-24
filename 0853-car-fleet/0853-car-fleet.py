class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        cars = sorted(zip(position,speed), reverse=True)
        st=[]

        for pos,sp in cars:
            time=float(target-pos)/sp
            st.append(time)

            if len(st)>=2 and st[-1]<=st[-2]:
                st.pop()
        
        return len(st)
