# https://leetcode.com/problems/target-sum/

from copy import copy
from typing import List

class Solution:
    def __init__(self):
        self.s = 0
        self.memo = {}
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self.aux(nums, target)

    def aux(self, nums1, target):
        nums = copy(nums1)
        x = nums.pop()
        
        if len(nums) == 0:
            return int(target == x) + int(target == -x)

        k1 = tuple((tuple(nums), target + x))
        k2 = tuple((tuple(nums), target - x))

        if self.memo.get(k1) is None:
            v1 = self.aux(nums, target + x)
            self.memo[k1] = v1

        if self.memo.get(k2) is None:
            v2 = self.aux(nums, target - x)
            self.memo[k2] = v2

        return self.memo[k1] + self.memo[k2]

