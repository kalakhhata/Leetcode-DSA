class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt=1
        org_mon=1
        mon=1
        money=0
        for i in range(n):
            if i!=0 and i%7==0:
                mon=org_mon+1
                org_mon+=1
            money+=mon
            mon+=1
        
        return money
        