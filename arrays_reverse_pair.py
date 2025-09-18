class Solution(object):
    def reversePairs(self, nums):
        def merge_sort(start, end):
            if start >= end:
                return 0
            
            mid = (start + end) // 2
            count = merge_sort(start, mid) + merge_sort(mid + 1, end)

            j = mid + 1
            for i in range(start, mid + 1):
                while j <= end and nums[i] > 2 * nums[j]:
                    j += 1
                count += (j - (mid + 1))
            
            temp = []
            i, j = start, mid + 1
            while i <= mid and j <= end:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1
            while i <= mid:
                temp.append(nums[i])
                i += 1
            while j <= end:
                temp.append(nums[j])
                j += 1
            
            nums[start:end+1] = temp
            return count

        return merge_sort(0, len(nums) - 1)