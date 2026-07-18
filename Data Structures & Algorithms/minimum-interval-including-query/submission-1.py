import heapq
from typing import List

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x: x[0])
        
        # Sort queries but remember original indices
        sorted_queries = sorted(range(len(queries)), key=lambda i: queries[i])
        
        result = [-1] * len(queries)
        min_heap = []  # (length, right)
        i = 0  # pointer into intervals
        
        for q_idx in sorted_queries:
            q = queries[q_idx]
            
            # Add all intervals that start at or before q
            while i < len(intervals) and intervals[i][0] <= q:
                left, right = intervals[i]
                length = right - left + 1
                heapq.heappush(min_heap, (length, right))
                i += 1
            
            # Remove intervals that end before q (no longer valid)
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)
            
            # Top of heap is the smallest valid interval
            if min_heap:
                result[q_idx] = min_heap[0][0]
        
        return result