# https://leetcode.com/problems/two-sum
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)

        lo, hi = 0, len(nums)-1
        store = None
        while lo < hi:
            if sorted_nums[lo] + sorted_nums[hi] == target:
                store = (lo, hi)
            
            if sorted_nums[lo] + sorted_nums[hi] > target:
                hi -=1

            else:
                lo += 1

        lo, hi = None, None
        for idx, el in enumerate(nums):
            if el == sorted_nums[store[0]] and lo is None:
                lo = idx
                

            elif el == sorted_nums[store[1]] and hi is None:
                hi = idx

        return [lo, hi]
