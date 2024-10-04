# https://leetcode.com/problems/unique-paths-ii/
from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # dp[i,j] = number of paths from cell [i, j] to (m,n)
        dp = {}
        
        m,n = len(obstacleGrid), len(obstacleGrid[0])
        dp[(m-1, n-1)] = 1

        for x in range(m):
            for y in range(n):
                if obstacleGrid[x][y]:
                    dp[(x,y)] = 0

        def unique_paths(i,j):
            if (i,j) in dp:
                return dp[(i,j)]

            if i >= m or j >= n:
                return 0

            dp[(i,j)] = unique_paths(i, j+1) + unique_paths(i+1, j)

            return dp[(i,j)]

        return unique_paths(0,0)
