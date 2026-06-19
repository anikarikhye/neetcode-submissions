class Solution:
    def isPalindrome(self, s: str) -> bool:
        string=""
        for i in s:
            if (i.isalnum()):
                string+=i
        length=len(string)
        count_till= (length//2)+1
        if length<=1:
            return True
        for i in range(0,count_till):
            if(string[i].lower()!=string[length-i-1].lower()):
                return False
        return True