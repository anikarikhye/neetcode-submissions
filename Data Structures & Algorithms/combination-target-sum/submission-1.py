from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()                          
        result = []
        path = []

        def check(start, remaining):
            if remaining == 0:              
                result.append(path[:])
                return

            for i in range(start, len(nums)):
                if nums[i] > remaining:      
                    break                   
                path.append(nums[i])
                check(i, remaining - nums[i])
                path.pop()

        check(0, target)
        return result













        