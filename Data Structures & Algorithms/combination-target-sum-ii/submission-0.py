from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()                 
        result = []
        path = []

        def calculate(start, remaining):
            if remaining == 0:             
                result.append(path[:])
                return

            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break                 
                if i > start and candidates[i] == candidates[i - 1]:
                    continue             
                path.append(candidates[i])                      
                calculate(i + 1, remaining - candidates[i])     
                path.pop()                                       

        calculate(0, target)
        return result

        

        