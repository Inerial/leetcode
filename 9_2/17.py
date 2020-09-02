class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz',
        }
        result = []
        if digits == '':
            return result
        def dfs(index, s):
            if len(digits) == index:
                result.append(s)
                return
            for j in dic[digits[index]]:
                dfs(index+1, s+j)
                
        dfs(0, '')
        return result