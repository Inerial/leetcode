# class Solution:
#     def numJewelsInStones(self, J: str, S: str) -> int:
#         ans = 0
#         cnt = collections.Counter(list(S))
        
#         for c in J:
#             if c in cnt:
#                 ans += cnt[c]
#         return ans
    
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum((i in J) for i in S)