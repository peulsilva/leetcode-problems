# https://leetcode.com/problems/ones-and-zeroes/
from typing import List
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        def count_zeros_ones(s: str):
            n_zeros = 0
            for c in s:
                if c == '0':
                    n_zeros +=1
            
            return n_zeros, len(s) - n_zeros

        dp = {}

        def solve(i, curr_ones, curr_zeros):
            if i >= len(strs):
                return 0

            if (i, curr_ones, curr_zeros) in dp:
                return dp[(i, curr_ones, curr_zeros)]

            zeros, ones = count_zeros_ones(strs[i])

            option1 = 0

            if  curr_ones + ones <= n and curr_zeros + zeros <= m:
                option1 = 1 + solve(i+1, curr_ones + ones, curr_zeros + zeros)
            

            option2 = solve(i+1, curr_ones, curr_zeros)
            dp[(i, curr_ones, curr_zeros)] = max(option1,option2)

            return max(option1,option2)

        return solve(0,0,0)
        