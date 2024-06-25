# https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum

from typing import List
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        nums_2 = [[idx, num ]for idx, num in enumerate(nums)]
        nums_2 = sorted(
            nums_2,
            reverse = True,
            key = lambda x: x[1]
        )
        n = len(nums)
        out_idx = []
        for i in range(k):
            out_idx.append(nums_2[i][0])

        out_idx = sorted(out_idx)

        out = []
        for i in out_idx:
            out.append(nums[i])

        return out
    

        