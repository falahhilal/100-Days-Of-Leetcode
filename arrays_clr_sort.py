class Solution(object):
    def sortColors(self, nums):
        n=len(nums)
        i=0
        for _ in range (n):
            if nums[_]==0:
                nums[i],nums[_]=nums[_],nums[i]
                i+=1
        for _ in range (n):
            if nums[_]==1:
                nums[i],nums[_]=nums[_],nums[i]
                i+=1