# https://leetcode.com/problems/longest-increasing-subsequence
from typing import List

class Solution:
    def __init__(self):
        self.memo = {}

    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        LIS =  [1]*n

        for l in range(n-1, -1, -1):
            for r in range(l+1, n):
                if nums[l]< nums[r]:
                    LIS[l] = max(LIS[l], 1+ LIS[r])

        return max(LIS)
    
# solution 2
    
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # memo[i]: length of LIS from 0 to [i]
        memo = [1 for i in nums]
        n = len(nums)

        for j in range(1,n):
            # j > i
            for i in range(j):

                if nums[j] > nums[i]:
                    memo[j] = max(memo[j], memo[i] + 1)

        return max(memo) 

