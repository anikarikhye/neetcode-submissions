class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter 
        
        count = Counter(s1)
        count2 = count.copy() 
        
        
        for index in range(0, len(s2) - len(s1) + 1): 
            for i in range(index, index + len(s1)):
                
                if s2[i] in count: 
                    count[s2[i]] -= 1
                    if max(count.values()) == 0:
                        return True
                        
           
            count = count2.copy() 
            
        return False



                