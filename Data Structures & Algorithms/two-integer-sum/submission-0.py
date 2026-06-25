from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict(int)
        for i, b in enumerate(nums):
            a = target - b
            if a in d:
                return [d[a], i]
            d[b] = i
        return []
        