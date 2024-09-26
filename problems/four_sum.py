# https://leetcode.com/problems/4sum/

from typing import List

# O(N^3) time O(1) space
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums = sorted(nums)
        ans = set()

        for i in range(n):
            for j in range(i+1, n):
                l,r = j+1, n-1

                while l < r:
                    four_sum = nums[i] + nums[j] + nums[l] + nums[r]
                    
                    
                    if four_sum < target:
                        l += 1

                    elif four_sum > target:
                        r-= 1

                    else:
                        ans.add((nums[i], nums[l], nums[r], nums[j]))
                        l+=1
                        r-=1


        return ans
             

# O(N²logN) time O(N²) time
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        # two_sums = [nums[i]+nums[j], i, j]
        two_sums = []
        visited = set()

        ans = set()

        for i in range(n):
            for j in range(i+1, n):
                two_sums.append([nums[i]+nums[j], i, j])
        
        two_sums = sorted(two_sums, key = lambda x: x[0]) # O(N^2 log N)
        l,r = 0, len(two_sums)-1
        
        def four_sums(l,r):
            if (l,r) in visited:
                return
            if r <= l:
                return
            
            visited.add((l,r))

            partial_sum = two_sums[l][0] + two_sums[r][0]

            if partial_sum < target:
                four_sums(l+1, r)
                

            elif partial_sum > target:
                four_sums(l,r-1)
                

            else : # partial_sum == target
                _, i,j = two_sums[l]
                _, k,m = two_sums[r]
                # print("indexes:")
                # print(i,j,k,m)
                # print("numbers")
                # print(nums[i], nums[j], nums[k], nums[m])

                if (i != k) and (i!=m) and (j != k) and (j != m):
                    ans.add(tuple(sorted([nums[i], nums[j], nums[k], nums[m]])))

                four_sums(l,r-1)
                four_sums(l+1,r)
        
        four_sums(0, len(two_sums)-1)
        return ans