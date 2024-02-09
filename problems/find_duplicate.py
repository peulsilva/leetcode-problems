# https://leetcode.com/problems/find-the-duplicate-number

from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            idx = abs(nums[i])

            if nums[idx] < 0:
                return idx
            
            nums[idx ] *= -1

        return n

        