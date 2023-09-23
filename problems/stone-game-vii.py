# https://leetcode.com/problems/stone-game-vii/
from collections import deque
from copy import copy


class Solution(object):
    def __init__(self):
        self.memo = {}
    def stoneGameVII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones = deque(stones)
        a = self.get_diff(stones, 1)
        return a 


    def get_diff(self, stones, turn):
        if len(stones) == 2:
            return max(stones) * turn

        s = sum(stones)
        s_left = copy(stones)
        left_choice = s_left.popleft()
        new_sum_left = s - left_choice

        s_right = copy(stones)
        right_choice = s_right.pop()
        new_sum_right = s - right_choice

        key_left = tuple((tuple(s_left), -1* turn))
        if self.memo.get(key_left) is not None:
            diff_left = self.memo[key_left]
        else:
            diff_left = self.get_diff(s_left, -1* turn)
            self.memo[key_left] = diff_left

        key_right = tuple((tuple(s_right), -1* turn))
        if self.memo.get(key_right) is not None:
            diff_right = self.memo[key_right]
        else:
            diff_right = self.get_diff(s_right, -1*turn)
            self.memo[key_right] = diff_right

        if turn == 1:
            
            return max(
                new_sum_left + diff_left,
                new_sum_right + diff_right
            )

        if turn == -1:
            return min(
                -new_sum_left + diff_left,
                -new_sum_right + diff_right
            )

    @staticmethod
    def get_score(stones, diff, s, turn):
        
        if len(stones) == 2:
            return diff + max(stones) * turn

        s_left = copy(stones)
        left_choice = s_left.popleft()
        new_sum_left = s - left_choice

        s_right = copy(stones)
        right_choice = s_right.pop()
        new_sum_right = s - right_choice

        if turn == 1:
            
            
            return max(
                Solution.get_score(s_left, diff + new_sum_left, new_sum_left , -1),
                Solution.get_score(s_right, diff + new_sum_right, new_sum_right, -1)
            )
        
        if turn == -1:
            return min(
                Solution.get_score(s_left, diff - new_sum_left, new_sum_left , 1),
                Solution.get_score(s_right, diff - new_sum_right, new_sum_right, 1)
            )