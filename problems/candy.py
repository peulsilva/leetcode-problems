class Solution:
    def candy(self, ratings: List[int]) -> int:
        # iterate through the array from left -> right than left <- right
        n = len(ratings)
        ans = [1 for i in range(n)]

        for i in range(1,n):
            if ratings[i] > ratings[i-1]:
                ans[i] = ans[i-1] + 1

        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                ans[i] = max(ans[i+1] + 1, ans[i])

        return sum(ans)