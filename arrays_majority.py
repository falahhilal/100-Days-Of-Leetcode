#https://leetcode.com/problems/majority-element/
import math 
class Solution(object):
    def majorityElement(self, nums):
        n=len(nums)
        ma=0
        temp=0
        for i in range (n):
            count=1
            for j in range (i+1,n):
                if nums[i]==nums[j]:
                    count+=1
            if count>ma:
                ma=count
                temp=nums[i]
        return temp