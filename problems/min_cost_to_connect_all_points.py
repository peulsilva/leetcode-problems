from typing import List


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for i in range(n)]

    def find(self, i):
        while i!= self.parent[i]:
            i = self.parent[i]
        
        return i

    def union(self, i, j):
        class_i = self.find(i)
        class_j = self.find(j)

        if class_i != class_j:
            if self.rank[class_i] > self.rank[class_j]:
                self.parent[class_j] = class_i

            elif self.rank[class_j] > self.rank[class_i]:
                self.parent[class_i] = class_j

            else:
                self.parent[class_j] = class_i
                self.rank[class_i]+= 1

# Kruskal's Algorithm
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        uf = UnionFind(n)
        total_distance = 0

        distances = []
        for i in range(n):
            for j in range(i+1,n):
                d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]) 
                distances.append([d, i,j])

        sorted_d = sorted(distances, key = lambda x: x[0])

        m = len(distances)

        for el in sorted_d:
            d, i, j = el
            if uf.find(i) != uf.find(j):
                uf.union(i, j)
                total_distance += d

        return total_distance
        