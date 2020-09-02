class Solution:
    def check(self, grid, i, j):
        if grid[i][j] == '0':
            return
        grid[i][j] = '0'
        if i-1 >= 0:
            self.check(grid, i-1, j)
        if i+1 < len(grid):
            self.check(grid, i+1, j)
        if j-1 >= 0:
            self.check(grid, i, j-1)
        if j+1 < len(grid[i]):
            self.check(grid, i, j+1)
        return
    
    def numIslands(self, grid: List[List[str]]) -> int:
        output = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '0':
                    continue
                else:
                    output += 1
                    self.check(grid, i ,j)
        
        return output