class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        left = 0
        right = len(height)-1
        left_best = height[left]
        right_best = height[right]
        answer = 0
        best = sorted(set(height))[-1]
        if len(height) >= 3:      
            while left < right:
                if height[left] < best or (height[left] == height[right]):
                    left += 1
                if height[right] < best:
                    right -= 1
                if height[left] < left_best:
                    answer += left_best - height[left]
                elif height[left] > left_best:
                    left_best = height[left]
                if left != right:
                    if height[right] < right_best:
                        answer += right_best - height[right]
                    elif height[right] > right_best:
                        right_best = height[right]
        return answer