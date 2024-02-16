# https://leetcode.com/problems/partition-equal-subset-sum
from typing import List

class Solution:

    def canPartition(self, nums: List[int]) -> bool:
        memo = {}
        if sum(nums) % 2 != 0:
            return False
        def can_partition(nums, s_l, s, n):
            s_r = s - s_l
            if s_l == s_r:
                return True

            if n == len(nums):
                return s_l == s_r


            k = tuple((s_l, n+1))
            
            if memo.get(k) is None:
                memo[k] = can_partition(nums, s_l + nums[n], s, n+1) or can_partition(nums, s_l, s, n+1)

            
            return memo[k]
            

        return can_partition(nums, 0, sum(nums), 0)