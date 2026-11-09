class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.calculate(0, [[]], nums)

    def calculate(self, i, result, nums):
        if i == len(nums):
            return result
        element = nums[i]
        current = []
        for item in result:
            current.append(item)              
            current.append(item + [element])  
        return self.calculate(i + 1, current, nums)

