class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l=list(set(nums))
        ans=[]
        count=[]
        d={}
        
        for i in range(len(l)):
            key=l[i]
            value=(nums.count(l[i]))
            d[key]=value
            count.append(value)
        count.sort()
        for i in range(k):
            value=count[len(count)-1-i]
            for i,j in d.items():
                if j==value:
                    ans.append(i)
        return(list(set(ans)))

            


        
            

            

        
        