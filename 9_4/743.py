class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        visits = {}
        d = collections.deque()
        dic = collections.defaultdict(list)
        for i, j, k in times:
            dic[i].append([j,k])
        d.append([K, 0])
        
        while len(d) > 0:
            now, now_time = d.popleft()
            if now not in visits:
                visits[now] = now_time
            elif visits[now] > now_time:
                visits[now] = now_time
            else:
                continue
            for i, j in dic[now]:
                d.append([i, now_time+j])
        return -1 if len(visits.keys()) != N else max(visits.values())