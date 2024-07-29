# https://leetcode.com/problems/permutations/
from typing import List

from copy import copy
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        paths = []

        def solve(curr_nums, curr_path):
            if len(curr_nums) == 0:
                paths.append(curr_path)

            for idx, el in enumerate(curr_nums):
                c = copy(curr_nums)
                c.pop(idx)

                p = copy(curr_path)
                p.append(el)

                solve(c, p)

        solve(nums, [])
        return paths