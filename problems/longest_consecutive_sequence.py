# https://leetcode.com/problems/longest-consecutive-sequence
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest_consecutive = 0

        for el in nums:
            if el - 1 not in nums:
                length = 0
                i = 0
            
                while el + i in nums:
                    length += 1
                    i+=1
                
                longest_consecutive = max(length, longest_consecutive)

        return longest_consecutive
        
        