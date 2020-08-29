# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         ans = 0
#         while len(prices) > 1:
#             now = prices.pop(0)
#             ans = max(ans, max(prices) - now)
#         return ans

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low, top, ans = None, None, 0
        for num in prices:
            if low is None or top is None:
                low, top = num,num
                continue
            if low > num:
                if ans < top - low:
                    ans = top - low
                low = num
                top = num
            if top < num:
                top = num
        if low is not None and ans < top - low:
            ans = top - low
        return ans