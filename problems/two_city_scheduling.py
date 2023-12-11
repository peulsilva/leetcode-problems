# https://leetcode.com/problems/two-city-scheduling
from typing import List
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        sorted_costs_dif = sorted(
            costs,
            key = lambda x: x[0] - x[1]
        )
        n = len(costs)//2

        total_costs = 0
        for i in range(n):
            total_costs += sorted_costs_dif[i][0] + sorted_costs_dif[n+i][1]

        return total_costs