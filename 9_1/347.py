class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt, ans = collections.Counter(nums).most_common(k), []
        for key, val in cnt:
            ans.append(key)
        return ans
        