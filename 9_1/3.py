class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cnt = {}
        left = ans = 0
        
        for i , c in enumerate(s):
            if c not in cnt:
                cnt[c] = i
            else:
                if left < cnt[c]+1:
                    left = cnt[c]+1
                cnt[c] = i
            if i-left+1 > ans:
                ans = i - left + 1
            print(left, i ,ans)
        
        return ans