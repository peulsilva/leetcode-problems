# https://leetcode.com/problems/gas-station/
from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # we want to start at the the last negative roll
        diff = [gas[i] - cost[i] for i in range(len(gas))]
        if sum(diff) < 0:
            return -1
        n = len(gas) 
        total = 0
        idx= 0
        for i, d in enumerate(diff):
            total += d

            if total < 0:
                total = 0
                idx = (i +1 )
            
        return idx