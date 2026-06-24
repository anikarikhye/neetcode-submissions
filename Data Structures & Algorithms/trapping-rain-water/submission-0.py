class Solution:
    def trap(self, height: List[int]) -> int:
        total_area=0
        for i in range(0,len(height)):
            left= 0 if (i<1) else max(height[0:i])
            right=max(height[i+1:]) if (i<len(height)-1) else 0
            area= min(left,right)- height[i]
            area=0 if (area<1) else area
            total_area+=area
        return total_area

        