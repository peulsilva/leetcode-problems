# https://leetcode.com/problems/valid-sudoku
from typing import List
class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        rows = [set() for i in range(n)]
        cols = [set() for i in range(n)]
        sub_boxes = [set() for i in range(n)]


        for i in range(n):
            for j in range(n):
                el = board[i][j]
                k = i // 3 + 3* (j //3)
                if (el == '.'):
                    continue
                print(i,j,k)
                if (el in rows[i] or el in cols[j] or el in sub_boxes[k]):
                    return False
                
                rows[i].add(el)
                cols[j].add(el)
                sub_boxes[k].add(el)

        return True
        