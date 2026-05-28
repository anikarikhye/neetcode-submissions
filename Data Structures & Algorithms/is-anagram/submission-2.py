class Solution:
    def isAnagram(self, s1, s2):
        if len(s1) != len(s2):
            return False

        freq = {}
        for char in s1:
            freq[char] = freq.get(char, 0) + 1

        for char in s2:
            if char not in freq:
                return False
            freq[char] -= 1
            if freq[char] < 0:
                return False

        return True