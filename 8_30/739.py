## 온도가 올라갈때까지 기다려야되는 일수
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        answer = [0] * len(T)
        stack = []
        for i , cur in enumerate(T):
            # 해당 위치 온도가 현재온도보다 낮으면
            # 해결하고 빼버림
            while stack and cur > T[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            # 해결 안된 날 스택에 매번 채워짐
            stack.append(i)
            
        return answer