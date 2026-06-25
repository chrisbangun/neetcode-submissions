# [1, 2, 4, 6]
# [1, 2, 8, 48]
# [48,48,24,6]
# [48,24,12,8]
class Solution:
    def get_cum_prod(self, arr: List[int]) -> List[int]:
        running_prod = 1
        cum_prd = []
        for val in arr:
            running_prod = running_prod * val
            cum_prd.append(running_prod)
        return cum_prd
        
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cum_prd_right = self.get_cum_prod(nums[::-1])[::-1]
        left_prod = 1
        answers = [1] * len(nums)
        for i, val in enumerate(nums):
            right_prod = 1 if i + 1 >= len(nums) else cum_prd_right[i + 1]
            ans = left_prod * right_prod
            answers[i] = ans
            left_prod = left_prod * val
        return answers



        