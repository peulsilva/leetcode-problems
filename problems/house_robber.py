# https://leetcode.com/problems/house-robber/
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        self.memo = {}
        return self.solution(nums,0)

    def solution(self, nums, l):
        if l == len(nums) - 1:
            return nums[-1]

        if l >= len(nums):
            return 0
        
        if self.memo.get(l+2) is None:
            self.memo[l+2] = self.solution(nums, l+2)

        if self.memo.get(l+1) is None:
            self.memo[l+1] = self.solution(nums, l+1)

        m1 = nums[l] + self.memo[l+2]
        m2 = self.memo[l+1]

        return max(m1,m2)
