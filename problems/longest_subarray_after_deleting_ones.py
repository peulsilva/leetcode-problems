# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element
from typing import List
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeros = []
        n = len(nums)
        for idx, el in enumerate(nums):
            if el == 0:
                zeros.append(idx)

        if len(zeros) == 0:
            return n - 1

        if len(zeros) == 1:
            return n-1

        m = max(zeros[1]-1, n - zeros[-2]-2)
        for idx_zero in range(1,len(zeros)-1):
            m = max(m, zeros[idx_zero+1] - zeros[idx_zero - 1]-2 )
        
        return m