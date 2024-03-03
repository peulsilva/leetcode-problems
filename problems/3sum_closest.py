# https://leetcode.com/problems/3sum-closest/

from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = 1e10

        nums = sorted(nums)
        n = len(nums)

        for (idx, a) in enumerate(nums):

            l, r = idx + 1, n - 1

            while l < r:
                
                three_sum = a + nums[l] + nums[r]

                if abs(three_sum - target) < abs(closest - target):
                    closest = three_sum

                if three_sum > target:
                    r -=1
                    continue

                if three_sum <= target:
                    l += 1

        return closest