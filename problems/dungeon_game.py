# https://leetcode.com/problems/dungeon-game/
from typing import List

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])

        dp = {}

        def solve(i,j):
            # returns the minimum health needed to go from (i,j) to (m-1,n-1)
            if (i,j) in dp:
                return dp[(i,j)]

            if i >= m:
                return 1e9
            
            if j >= n:
                return 1e9


            if (i,j) == (m-1, n-1):
                return max(1, 1-dungeon[m-1][n-1])


            if dungeon[i][j] > 0:
                
                option1 = max(-dungeon[i][j] + solve(i+1,j), 1)
                option2 = max(-dungeon[i][j] + solve(i, j+1), 1)

            else:

                option1 = max(-dungeon[i][j] + solve(i+1,j), -dungeon[i][j] + 1)
                option2 = max(-dungeon[i][j] + solve(i, j+1), -dungeon[i][j]+ 1)

            dp[(i,j)] = min(option1, option2)

            return dp[(i,j)]

        ans= solve(0,0)
        return ans
        