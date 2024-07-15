from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals = sorted(intervals, key = lambda x: x[0])
        clusters = [intervals[0]]
        last_start, last_end = intervals[0]
        cluster_idx = 0

        for i,(start, end) in enumerate(intervals):
            if i ==0:
                continue

            if start <= last_end:
                # merge
                cluster_start = clusters[cluster_idx][0]
                cluster_end = max(end, last_end)
                clusters[cluster_idx] = [cluster_start, cluster_end]

                last_start, last_end = start, cluster_end

            else:
                clusters.append([start, end])
                cluster_idx+=1

                last_start, last_end = start, end

        return clusters