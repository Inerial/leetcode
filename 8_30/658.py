class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) <= k:
            return arr
        answer = collections.deque()
        for i in range(len(arr)):
            answer.append(arr[i])
            if len(answer) > k:
                if abs(answer[0]-x) < abs(answer[-1]-x):
                    answer.pop()
                    break
                elif abs(answer[0]-x) == abs(answer[-1]-x):
                    answer.pop()
                else:
                    answer.popleft()
        
        return answer

            