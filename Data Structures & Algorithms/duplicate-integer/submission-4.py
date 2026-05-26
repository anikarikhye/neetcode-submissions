class Solution:
    def hasDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False
