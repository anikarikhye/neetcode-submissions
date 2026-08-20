'''
Steps
Step-1: Since we are checking for k closest points nearest to the origin, the values of x2 and y2 are 0
Step-2: Hence the values to now optimize for are (x1)^2-(y1)^2 which expands to (x1+x2)(x1-x2).
Step-3: By choosing values of x1 and y1 that have the least differnce between them but at the same time x1 and y1 also need to be the smallest values in the array.
Step-4: Create the answer for every point in the array and convert to heap and pop out the k closest points.
'''
import heapq

class Solution:
    def calculate(self, node):
        distance = (node[0])**2 + (node[1])**2
        return distance

    def create(self, array):
        heap = []
        for node in array:
            result = self.calculate(node)
            heap.append((result, node))
        return heap

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = self.create(points)
        heapq.heapify(heap)
        result = []
        for i in range(0, k):
            distance, point = heapq.heappop(heap)
            result.append(point)
        return result
        