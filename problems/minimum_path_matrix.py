# https://leetcode.com/problems/minimum-path-sum/
from typing import List

class Solution:

    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])

        # min_path_matrix[i][j] : minimum path from (i,j) to the destination 

        min_path_matrix = [[1e10 for i in range(n)] for i in range(m)]
        min_path_matrix[m-1][n-1] = grid[m-1][n-1]

        # fill the table from right bottom to the left top

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if (i, j) == (m-1, n-1):
                    continue

                if i == m - 1:
                    min_path_matrix[i][j] = min_path_matrix[i][j+1] + grid[i][j]
                    continue

                if j == n -1:
                    min_path_matrix[i][j] = min_path_matrix[i+1][j] + grid[i][j]
                    continue
                
                min_path_matrix[i][j] = min(
                    min_path_matrix[i+1][j]+ grid[i][j], 
                    min_path_matrix[i][j+1]+ grid[i][j]    
                ) 

        return min_path_matrix[0][0]