class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        
        res=[]

        def dfs(start,ans,value,prev):
            #base-case
            if start==len(num):
                if value==target:
                    res.append(ans)
                return
            
            for end in range(start,len(num)):
                if num[start]=='0' and end>start:
                    break
                st=num[start:end+1]
                vl=int(st)
                
                if start==0:
                    dfs(end+1,st,vl,vl)
                else:
                    #addition 
                    dfs(end+1,ans+'+'+st,value+vl,vl)
                    #sub
                    dfs(end+1,ans+'-'+st,value-vl,-vl)
                    #multiplication
                    dfs(end+1,ans+'*'+st,value-prev+prev*vl,prev*vl)
            
        dfs(0,'',0,0)
        return res