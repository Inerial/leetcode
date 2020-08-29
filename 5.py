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