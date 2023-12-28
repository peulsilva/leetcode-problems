# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 2:
            return min(nums)

        l, r = 0, len(nums) - 1
        m = (l+r)//2

        if nums[0] <= nums[m] and nums[r] >= nums[m]:
            return nums[0]
        while l < r:
            if (r-l) == 1:
                return min(nums[r], nums[l])
            m = (l+r)//2
            if nums[l] < nums[m] and nums[r] < nums[m]:
                l = m
                continue

            if nums[l] > nums[m] and nums[r] > nums[m]:
                r = m
                continue
            
            if nums[m] > nums[l] and nums[r] < nums[m]:
                l = m
            
            elif nums[m] < nums[l] and nums[r] > nums[m]:
                r = m