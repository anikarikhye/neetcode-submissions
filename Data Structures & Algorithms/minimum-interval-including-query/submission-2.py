import heapq
from typing import List

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()  # sort by start time
        min_heap = []  # (length, end)
        res = {}
        i = 0  # pointer into intervals

        for q in sorted(queries):
            # add all intervals that start <= q
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(min_heap, (r - l + 1, r))
                i += 1

            # remove intervals that end before q
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)

            # smallest valid interval length, or -1
            res[q] = min_heap[0][0] if min_heap else -1

        return [res[q] for q in queries]
        