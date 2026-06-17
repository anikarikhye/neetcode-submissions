import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[1]*len(nums)       
        for i in range(0, len(nums)):
            p=math.prod(nums[0:i])*math.prod(nums[i+1:])
            output[i]=p
        return(output)
                
                


        
        
        
        
        
