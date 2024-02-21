# https://leetcode.com/problems/subarray-sum-equals-k/
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)

        if n == 1:
            return int(nums[0] == k)

        sums = {0 : 1}
        partial_sum = 0
        ans = 0

        for i in range(n):
            partial_sum += nums[i]

            if partial_sum - k in sums:
                ans += sums[partial_sum - k]
                
            if partial_sum not in sums:
                sums[partial_sum] = 1
            
            else:
                sums[partial_sum] += 1

                

        return ans