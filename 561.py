# import numpy as np
# class Solution:
#     def arrayPairSum(self, nums: List[int]) -> int:
#         nums = np.array(sorted(nums))
#         return sum(nums.reshape(-1,2)[:, 0])
##  속도가 어림도 없음

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)[::2]
        return sum(nums)

