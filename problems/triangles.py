# https://leetcode.com/problems/triangle/description

from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # constructing graph
        h = len(triangle)
        memo = dict()

        for i, row in enumerate(triangle):
            height = h - i

            if i == 0:
                memo[(height,0)] =triangle[0][0]

            else:
                for j, dist in enumerate(row):
                    options = []
                    if (height+1, j) in memo:
                        options.append(memo[(height+1, j)]+ triangle[i][j])

                    if (height+1, j-1) in memo:
                        options.append(memo[(height+1, j-1)]+ triangle[i][j])

                    memo[(height, j)] =min(options)

        ans = 1e20

        for i in range(h):
            ans = min(ans, memo[(1, i)])

        return ans
                    
