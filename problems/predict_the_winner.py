# https://leetcode.com/problems/predict-the-winner/
from typing import List

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        memo = {}
        def max_profit(i, j, player):
            if (i,j, player) in memo:
                return memo[(i,j, player)]
            
            if i == j:
                return nums[i]

            if player == 1:

                option1 = nums[i] + max_profit(i+1,j, -player)
                option2 = nums[j] + max_profit(i, j-1, -player)
                memo[(i,j, player)] = max(option1, option2)

            else:
                option1 = max_profit(i+1,j, -player)
                option2 = max_profit(i, j-1, -player)

                memo[(i,j, player)] = min(option1, option2)

            return memo[(i,j, player)]

        profit =  max_profit(0, len(nums)-1, 1)
        
        return profit >= sum(nums) - profit