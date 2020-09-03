class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        dic = {}
        ans = ['JFK']
        for f, t in tickets:
            if f not in dic:
                dic[f] = [t]
            else:
                dic[f] += [t]
                dic[f].sort()
        
        print(dic)
        def dfs(s):
            if s not in dic:
                return
            for i in range(len(dic[s])):
                to = dic[s].pop(0)
                ans.append(to)
                dfs(to)
                if len(ans) == len(tickets)+1:
                    return
                dic[s] += [ans.pop()]
                
        dfs('JFK')
        
        return ans