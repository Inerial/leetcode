class Solution:
    def reverse(self, x: int) -> int:
        minus = ['']
        if x < 0:
            minus,  x = ['-'], abs(x)
        ans = int(''.join(minus + list(reversed(list(str(x))))))
        ## 문제가 overflow를 요구함 (c기준인듯)
        if ans < -(2**31) or ans > 2**31 - 1:
            ans = 0
        return ans