class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        
        def dfs(num):
            if len(num) == k:
                ans.append(num)
                return
            for i in range(num[-1]-1, 0, -1):
                dfs(num + [i])
            return
                
        for i in range(n, 0, -1):
            dfs([i])
            
        return ans