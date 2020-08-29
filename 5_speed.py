class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        while length > 0:
            left = 0
            right = left + length
            while right <= len(s):
                if s[left:right] == s[left:right][::-1]:
                    return s[left:right]
                left += 1
                right += 1
            length -= 1
            
        return ""
        
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left,right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        
        if len(s)< 2 or s == s[::-1]:
            return s
        
        result = ''
        for i in range(len(s) - 1):
            result =  max(result, expand(i,i), expand(i,i+1), key=len)
        return result