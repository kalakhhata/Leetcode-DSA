class Solution:
    def addDigits(self, num: int) -> int:
        seen=set()

        while num>9:
            num=self.sumOf(num)
        
        return num
    
    def sumOf(self,num):
        total=0

        while num>0:
            total+=(num%10)
            num=num//10
        return total
        