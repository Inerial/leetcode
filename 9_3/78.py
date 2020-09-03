class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        def dfs(index, n):
            if index == len(nums):
                return
            for i in range(index+1, len(nums)):
                ans.append(n + [nums[i]])
                dfs(i, n + [nums[i]])
            return
        
        for i, n in enumerate(nums):
            ans.append([n])
            dfs(i , [n])
        
        return ans