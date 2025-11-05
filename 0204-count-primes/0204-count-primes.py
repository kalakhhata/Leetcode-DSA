class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<3:
            return 0
        box=[True for _ in range(n+1)]
        box[0]=box[1]=box[n]=False

        p=2
        
        while p*p<=n:
            if box[p]:
                for i in range(p*p,n+1,p):
                    box[i]=False
            p+=1
        
        return sum(box)

        


        