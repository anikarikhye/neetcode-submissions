class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
       
        graph = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        visiting = set()   
        done = set()       

        def has_cycle(node):
            if node in visiting:
                return True       
            if node in done:
                return False       

            visiting.add(node)
            for neighbor in graph[node]:
                if has_cycle(neighbor):
                    return True
            visiting.remove(node)
            done.add(node)
            return False

        for course in range(numCourses):
            if has_cycle(course):
                return False
        return True