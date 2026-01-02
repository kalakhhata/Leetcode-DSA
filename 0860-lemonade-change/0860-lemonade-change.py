class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """

        if bills[0]!=5:
            return False
        
        five_d=0
        ten_d=0

        for bill in bills:
            if bill==5:
                five_d+=1
            elif bill==10:
                if five_d>0:
                    five_d-=1
                else:
                    return False
                ten_d+=1
            else:
                if five_d>0 and ten_d>0:
                    five_d-=1
                    ten_d-=1
                elif five_d>2:
                    five_d-=3
                else:
                    return False
        

        return True



        