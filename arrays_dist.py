#https://leetcode.com/problems/find-the-distance-value-between-two-arrays

class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        n=len(arr1)
        m=len(arr2)
        count=0
        for i in range (n):
            for j in range (m):
                if abs(arr1[i]-arr2[j]) < d or abs(arr1[i]-arr2[j])==d:
                    break
                if j==m-1:
                    count+=1
        return count 