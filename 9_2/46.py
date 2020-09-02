class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        flag = [0] * len(nums)
        def dfs(li):
            if len(li) == len(nums):
                ans.append(li)
                return
            for i, n in enumerate(nums):
                if flag[i] == 1:
                    continue
                flag[i] = 1
                dfs(li + [n])
                flag[i] = 0
        
        dfs([])
        return ans