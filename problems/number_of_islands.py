# https://leetcode.com/problems/number-of-islands/
from typing import List
class Solution:
    def __init__(self):
        self.visited = {}
    def get_neighbors(self, grid, i, j):
        m = len(grid)
        n = len(grid[0])

        upper_cell = (i - 1, j)
        lower_cell = (i + 1, j)
        left_cell = (i, j - 1)
        right_cell = (i, j+ 1)

        neighbors = []
        for cell in [upper_cell, lower_cell, left_cell, right_cell]:
            i, j = cell
            if i < 0 or i >= m:
                continue
            
            if j < 0 or j >= n:
                continue

            if grid[i][j] != '0':
                neighbors.append([i,j])

        return neighbors

    def DFS(self, grid, i,j):
        VISITED = 1

        queue = [(i,j)]
        while (len(queue) > 0):
            i,j = queue.pop()
            if self.visited.get(tuple((i,j))) is not None:
                continue

            self.visited[tuple((i,j))] = 1

            neighbors = self.get_neighbors(grid, i,j )

            for [x,y] in neighbors:
                queue.append([x,y])

            self.visited[tuple((i,j))] = VISITED
            
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        n_islands = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] != "0":
                    if self.visited.get(tuple((i,j))) is None:
                        n_islands +=1
                        self.DFS(grid,i,j)

        return n_islands
                        