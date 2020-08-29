# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         while len(nums) > 1:
#             num = nums.pop()
#             if (target-num) in nums:
#                 return [nums.index(target-num), len(nums)]
            
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        answer = None
        for i, num in enumerate(nums):
            if (target-num) in d:
                answer = [d[target-num][0], i]
            if num in d:
                d[num] += [i]
            else:
                d[num] = [i]
        return answer