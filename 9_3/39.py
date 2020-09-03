class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        def dfs(index, nums):
            for i in range(index, len(candidates)):
                n = candidates[i]
                if sum(nums) + n == target:
                    ans.append(nums + [n])
                    return
                elif sum(nums) + n > target:
                    return
                else:
                    dfs(i, nums + [n])
            return
        
        for i, n in enumerate(candidates):
            if n == target:
                ans.append([n])
                continue
            dfs(i, [n])
            
        return ans