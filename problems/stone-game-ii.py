# https://leetcode.com/problems/stone-game-ii/description/
from typing import List

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        dp = {}
        def get_piles(l, alice, M):
            # maximum amount of money alice can get from l to end
            if l >= len(piles):
                return 0

            if (l, alice, M) in dp:
                return dp[(l, alice, M)]

            ans = 0 if alice else 1e8
            count = 0

            for x in range(2*M):

                if l + x >= len(piles):
                    break

                count += piles[l+x]

                if alice:
                    ans = max(ans, count+get_piles(l+x+1, not alice, max(M, x+1)))
                
                if not alice:
                    ans = min(ans, get_piles(l+x+1, not alice, max(M, x+1)))

            dp[(l, alice, M)] = ans
            return ans

        ans = get_piles(0,True,1)
        return ans