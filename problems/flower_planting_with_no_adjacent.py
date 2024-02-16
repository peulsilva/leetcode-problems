# https://leetcode.com/problems/flower-planting-with-no-adjacent/

# Coloring graph: 
# Traverse the vertices and colors it with a color that 
# has not yet been used on its neighbors

from typing import List

class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        adjacency = {}

        colors = [-1 for i in range(n)]

        # constructing the graph
        for p in paths:
            x, y = p
            x-= 1
            y-= 1
            if adjacency.get(x) is None:
                adjacency[x] = set()

            if adjacency.get(y) is None:
                adjacency[y] = set()
            
            adjacency[x].add(y)
            adjacency[y].add(x)

        for k in range(n):
            used_colors = set()

            if not k in adjacency:
                colors[k] = 1
                continue
                
            for l in adjacency[k]:
                used_colors.add(colors[l])

            for i in range(1, 5):
                if i in used_colors: 
                    continue

                colors[k] = i
                break

        return colors