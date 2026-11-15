from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def check(path, summ, start):
            if summ > target:                    
                return
            if summ == target:                   
                result.append(path[:])
                return

            for i in range(start, len(nums)):
                path.append(nums[i])                 
                check(path, summ + nums[i], i)       
                path.pop()                           
        check([], 0, 0)
        return result




















        