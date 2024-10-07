# https://leetcode.com/problems/kth-largest-element-in-an-array
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def solve(l, k):
            
            pivot = l[0]
            x_greater = [x for x in l if x > pivot]
            x_equal = [x for x in l if x == pivot]
            x_less = [x for x in l if x < pivot]

            if k <= len(x_greater):
                return solve(x_greater, k)
            elif k <= len(x_greater) + len(x_equal):
                return pivot
            else:
                return solve(x_less, k - len(x_greater) - len(x_equal))

        return solve(nums, k)