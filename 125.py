class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for c in s:
            if c.isalnum():
                strs.append(c.lower())
        return strs == list(reversed(strs))