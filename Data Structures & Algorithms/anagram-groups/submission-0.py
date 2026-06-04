

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def is_anagram(s1, s2):
            if len(s1) != len(s2):
                return False
            count = {}
            for char in s1:
                count[char] = count.get(char, 0) + 1
            for char in s2:
                count[char] = count.get(char, 0) - 1
            return all(v == 0 for v in count.values())
        
        visited = set()
        output = []

        for i in range(len(strs)):
            if i in visited:
                continue
            
            group = [strs[i]]
            
            for j in range(i+1, len(strs)):
                if j in visited:
                    continue
                if is_anagram(strs[i], strs[j]):
                    group.append(strs[j])
                    visited.add(j)
            
            output.append(group)
        
        return output


# Test
sol = Solution()
print(sol.groupAnagrams(["act","pots","tops","cat","stop","hat"]))
# [["act","cat"], ["pots","tops","stop"], ["hat"]]