class Solution:
    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = s.index("#", i)
            length = int(s[i:j])
            res.append(s[j+1 : j+1+length])
            i = j + 1 + length
        return res