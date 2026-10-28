from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) != n - 1:
            return False

        
        return self.connected(n, edges)

    def connected(self, n, edges):
        
        neighbours = [[] for _ in range(n)]
        for a, b in edges:
            neighbours[a].append(b)
            neighbours[b].append(a)

        visited = set()
        self.explore(0, neighbours, visited)

      
        return len(visited) == n

    def explore(self, node, neighbours, visited):
        visited.add(node)
        for friend in neighbours[node]:
            if friend not in visited:
                self.explore(friend, neighbours, visited)


        