class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        visits = {}
        d = collections.deque()
        dic = collections.defaultdict(list)
        for i, j, k in flights:
            dic[i].append([j,k])
        d.append([src, 0, 0])
        
        while len(d) > 0:
            now, now_time, times = d.popleft()
            if times > K+1:
                continue
            if now not in visits:
                visits[now] = now_time
            elif visits[now] > now_time:
                visits[now] = now_time
            else:
                continue
            for i, j in dic[now]:
                d.append([i, now_time+j, times + 1])
        return -1 if dst not in visits else visits[dst]

### 743.py 실찍 변형