class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not len(nums):
            return 0
            
        nums_flag = {num: 0 for num in nums}
        max_len = 1
        for val in nums:
            if nums_flag.get(val, 0) != 0:
                continue
            # keep increasing by 1
            nums_flag[val] = 1
            right = val + 1
            while right in nums_flag and nums_flag[right] == 0:
                nums_flag[right] = 1
                right += 1
                
            # keep decreasing by 1
            left = val - 1
            while left in nums_flag and nums_flag[left] == 0:
                nums_flag[left] = 1
                left -= 1
                
            # print(left, right, val)
            max_len = max(max_len, right - left - 1)

        return max_len