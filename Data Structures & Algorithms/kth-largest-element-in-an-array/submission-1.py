'''
Steps
Step-1: Create a min heap with the negative of the numbers in an array.
Step-2: Run this loop k times and pop elements one by one and the negative of that number is the solution
'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap=[-num for num in nums]
        result=[]
        heapq.heapify(heap)
        for i in range (0,k):
            x=-(heapq.heappop(heap))
            result.append(x)
        return result[k-1]


        