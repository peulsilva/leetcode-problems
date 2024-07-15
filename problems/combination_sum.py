from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        paths = set()
        n = len(candidates)

        # search for paths in candidates[start:] that sums to target
        def solve(start, target, curr_path):
            if start >= n:
                return
            if target == 0:
                paths.add(curr_path)
                return 

            if target< 0: 
                return
            
            for idx, el in enumerate(candidates):
                if idx < start:
                    continue
                solve(idx, target - el, curr_path + ' ' +str(el))

        solve(0,target, '')
        arr_paths = []
        for path in paths:
            l = []
            for x in path.split(' '):
                try:

                    l.append(int(x))

                except:
                    pass

            arr_paths.append(l)
        return arr_paths