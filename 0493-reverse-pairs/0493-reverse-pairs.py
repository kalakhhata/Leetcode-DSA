class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.mergeSort(0,len(nums)-1,nums)
    
    def mergeSort(self,low,high,nums):
        cnt=0
        if low>=high:
            return cnt
        
        mid=(low+high)//2
        cnt=self.mergeSort(low,mid,nums)
        cnt+=self.mergeSort(mid+1,high,nums)
        #cnt+=self.countPairs(low,mid,high,nums)
        cnt+=self.merge(low,mid,high,nums)
        return cnt
    
    
    def merge(self,low,mid,high,nums):
        left=low
        right=mid+1
        cnt=0
        for i in range(low,mid+1):
            while right<=high and nums[i]>2*nums[right]:
                right+=1
            cnt+=right-(mid+1)
        
        right=mid+1
        temp=[]

        while left<=mid and right<=high:
            if nums[left]<=nums[right]:
                temp.append(nums[left])
                left+=1
            else:
                temp.append(nums[right])
                right+=1
        
        while left<=mid:
            temp.append(nums[left])
            left+=1
        
        while right<=high:
            temp.append(nums[right])
            right+=1
        
        for i in range(len(temp)):
            nums[low+i]=temp[i]
        
        return cnt
        