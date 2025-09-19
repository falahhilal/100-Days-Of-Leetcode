#https://leetcode.com/problems/monotonic-array/

class Solution(object):
    def isMonotonic(self, nums):
        n=len(nums)
        if n==1:
            return True
        for i in range (n-1):
            if nums[i] < nums[i+1] or nums[i] == nums[i+1]:
                if i==n-2:
                    return True
            else:
                break

        for i in range (n-1):
            if nums[i]>nums[i+1] or nums[i]==nums[i+1]:
                if i==n-2:
                    return True
            else:
                break
    
        return False