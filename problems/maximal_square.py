# https://leetcode.com/problems/maximal-square/
from typing import List

class Solution:
    def get_neighbours(self, i, j):
        return [[i-1, j-1], [i, j-1], [i-1, j]]

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)

        n = len(matrix[0])

        if m == 1:
            for j in range(n):
                if matrix[0][j] == '1':
                    return 1

            return 0

        if n == 1:
            for i in range(m):
                if matrix[i][0] == '1':
                    return 1

            return 0

        ans = 0

        for i in range(1,m):
            for j in range(1,n):

                if matrix[i][j] == "0" or matrix[i][j] == 0:
                    continue

                neighbours = self.get_neighbours(i,j)

                min_neighbours = 1e9
                for (x,y) in neighbours:
                    min_neighbours = min(int(matrix[x][y]), min_neighbours)

                matrix[i][j] = min_neighbours + 1
                if matrix[i][j] > ans : 
                    ans = matrix[i][j]

        if ans == 0:
            for i in range(m):
                for j in range(n):
                    if matrix[i][j] == '1': 
                        return 1

        return ans**2


        