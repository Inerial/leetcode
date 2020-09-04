# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         dic, check = collections.defaultdict(list), set()
#         for i, j in prerequisites:
#             dic[i].append(j)
            
#         def dfs(n):
#             if n in check:
#                 return False
#             check.add(n)
            
#             for y in dic[n]:
#                 if not dfs(y):
#                     return False
#             check.remove(n)
#             return True
            
#         for key in list(dic):
#             if not dfs(key):
#                 return False
#         return True

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dic, check = collections.defaultdict(list), set()
        visits = set()
        for i, j in prerequisites:
            dic[i].append(j)
            
        def dfs(n):
            if n in visits:
                return True
            if n in check:
                return False
            check.add(n)
            
            for y in dic[n]:
                if not dfs(y):
                    return False
            check.remove(n)
            visits.add(n)
            return True
            
        for key in list(dic):
            if not dfs(key):
                return False
        return True