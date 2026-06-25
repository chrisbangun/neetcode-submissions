class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False

        seen = set()
        for val in nums:
            if val in seen:
                return True
            seen.add(val)
        return False