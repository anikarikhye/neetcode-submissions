class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        left = 0
        max_freq = 0
        max_length = 0
        

        for right in range(len(s)):
            char = s[right]
            counts[char] = counts.get(char, 0) + 1
            
            
            max_freq = max(max_freq, counts[char])
            
           
            if (right - left + 1) - max_freq > k:
                counts[s[left]] -= 1
                left += 1
           
            max_length = max(max_length, right - left + 1)
            
        return max_length