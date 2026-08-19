'''
Steps
Step-1: Create a while loop that breaks when len(stones)=1
Step-2: At each iteration, create a min heap and put the largest two elements at the top
Step-4: Subtract the 2nd largest element from the largest element and replace the two elements with their difference
Step-5: Continue this recursively 
'''
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[-stone for stone in stones]
        heapq.heapify(heap)
        while len(heap)>1:
            x=-heapq.heappop(heap)
            y=-heapq.heappop(heap)
            difference=x-y
            if (difference!=0):
                heapq.heappush(heap,-difference)
        return -heap[0] if heap else 0

            


            
            


        